# Create your views here.
from datetime import datetime

from django.db.models.aggregates import Count
from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from asset.models import Asset
from asset.serializers import AssetSerializers
from . import models
from .models import ContactTracing
from .serializers import ContactTracingSerializer


class SocialDistancing(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        try:
            startdate = request.data.get("start")
            enddate = request.data.get("end")
            tagId = request.data.get("tagId")

            startEpoch = datetime.strptime(startdate, "%Y-%m-%d-%H:%M:%S").timestamp()
            print("startEpoch time ", startEpoch)
            endEpoch = datetime.strptime(enddate, "%Y-%m-%d-%H:%M:%S").timestamp()
            print("endEpoch time ", endEpoch)

            payload = []
            asset = Asset.objects.raw('select id from asset_asset where tagId = %s',[tagId])[0].id

            if asset != None:
                qry = 'select 1 as id, tag2_id from socialdistance_contacttracing where tag1_id = %s and epochTime between %s and %s group by tag2_id'
                # distinct_tag_list  = ContactTracing.objects.raw(qry,[asset.id, startEpoch, endEpoch])
                for tagList in ContactTracing.objects.raw(qry, [asset, startEpoch, endEpoch]):
                    print(tagList.tag2_id)
                    qry2 = 'select 1 as id, epochTime from socialdistance_contacttracing where tag1_id = %s and tag2_id = %s  and epochTime between %s and %s  group by epochTime order by epochTime'
                    result = ContactTracing.objects.raw(qry2, [asset, tagList.tag2_id, startEpoch, endEpoch])
                    count = 0
                    comptime = 0
                    duration = 0
                    startduration  = result[0].epochTime
                    print("[0] value : ", result[0].epochTime)
                    firsttime = result[0].epochTime
                    temptime = firsttime
                    for eventList in result:
                        comptime = eventList.epochTime
                        if comptime - firsttime > 15:
                            count = count+1
                            duration = duration+(firsttime-startduration)
                            startduration = comptime
                        firsttime = comptime

                    tag2_macid = Asset.objects.filter(id=tagList.tag2_id)[0].tagId

                    if duration > 0:
                        seconds = duration
                        sec = int(seconds % 60)
                        p2 = seconds / 60
                        min = int(p2 % 60)
                        hour = int(p2 / 60)
                        timing = "{}:{}:{}".format(hour, min, sec)

                        print("inside first append ")
                        payload.append({"tagId": tag2_macid, "eventStartTime": datetime.fromtimestamp(temptime),
                                                    "eventEndTime": datetime.fromtimestamp(comptime), "eventCount": count + 1,
                                                    "timestamp": timing})
                    else:
                        seconds = int(comptime-temptime)
                        sec = seconds % 60
                        p2 = seconds / 60
                        min = int(p2 % 60)
                        hour = int(p2 / 60)
                        timing = "{}:{}:{}".format(hour, min, sec)
                        print("in second append ")
                        payload.append({"tagId": tag2_macid, "eventStartTime": datetime.fromtimestamp(temptime),
                                        "eventEndTime": datetime.fromtimestamp(comptime), "eventCount": count + 1,
                                        "timestamp": timing})

            return Response({"result": payload}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)