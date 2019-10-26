# automatically generated by the FlatBuffers compiler, do not modify

# namespace: proto

import flatbuffers

class BrokerFeatures(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBrokerFeatures(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BrokerFeatures()
        x.Init(buf, n + offset)
        return x

    # BrokerFeatures
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BrokerFeatures
    def PublisherIdentification(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def PublisherExclusion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def SubscriberBlackwhiteListing(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def PatternBasedSubscription(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def PublicationTrustlevels(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def SubscriptionRevocation(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def SessionMetaApi(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def SubscriptionMetaApi(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def EventRetention(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def EventHistory(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def AcknowledgeEventReceived(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def AcknowledgeSubscriberReceived(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def PayloadTransparency(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # BrokerFeatures
    def PayloadEncryptionCryptobox(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def BrokerFeaturesStart(builder): builder.StartObject(14)
def BrokerFeaturesAddPublisherIdentification(builder, publisherIdentification): builder.PrependBoolSlot(0, publisherIdentification, 0)
def BrokerFeaturesAddPublisherExclusion(builder, publisherExclusion): builder.PrependBoolSlot(1, publisherExclusion, 0)
def BrokerFeaturesAddSubscriberBlackwhiteListing(builder, subscriberBlackwhiteListing): builder.PrependBoolSlot(2, subscriberBlackwhiteListing, 0)
def BrokerFeaturesAddPatternBasedSubscription(builder, patternBasedSubscription): builder.PrependBoolSlot(3, patternBasedSubscription, 0)
def BrokerFeaturesAddPublicationTrustlevels(builder, publicationTrustlevels): builder.PrependBoolSlot(4, publicationTrustlevels, 0)
def BrokerFeaturesAddSubscriptionRevocation(builder, subscriptionRevocation): builder.PrependBoolSlot(5, subscriptionRevocation, 0)
def BrokerFeaturesAddSessionMetaApi(builder, sessionMetaApi): builder.PrependBoolSlot(6, sessionMetaApi, 0)
def BrokerFeaturesAddSubscriptionMetaApi(builder, subscriptionMetaApi): builder.PrependBoolSlot(7, subscriptionMetaApi, 0)
def BrokerFeaturesAddEventRetention(builder, eventRetention): builder.PrependBoolSlot(8, eventRetention, 0)
def BrokerFeaturesAddEventHistory(builder, eventHistory): builder.PrependBoolSlot(9, eventHistory, 0)
def BrokerFeaturesAddAcknowledgeEventReceived(builder, acknowledgeEventReceived): builder.PrependBoolSlot(10, acknowledgeEventReceived, 0)
def BrokerFeaturesAddAcknowledgeSubscriberReceived(builder, acknowledgeSubscriberReceived): builder.PrependBoolSlot(11, acknowledgeSubscriberReceived, 0)
def BrokerFeaturesAddPayloadTransparency(builder, payloadTransparency): builder.PrependBoolSlot(12, payloadTransparency, 0)
def BrokerFeaturesAddPayloadEncryptionCryptobox(builder, payloadEncryptionCryptobox): builder.PrependBoolSlot(13, payloadEncryptionCryptobox, 0)
def BrokerFeaturesEnd(builder): return builder.EndObject()