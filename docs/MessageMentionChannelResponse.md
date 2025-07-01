# MessageMentionChannelResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**type** | **int** |  | 
**guild_id** | **str** |  | 

## Example

```python
from dc_rest.models.message_mention_channel_response import MessageMentionChannelResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MessageMentionChannelResponse from a JSON string
message_mention_channel_response_instance = MessageMentionChannelResponse.from_json(json)
# print the JSON string representation of the object
print(MessageMentionChannelResponse.to_json())

# convert the object into a dict
message_mention_channel_response_dict = message_mention_channel_response_instance.to_dict()
# create an instance of MessageMentionChannelResponse from a dict
message_mention_channel_response_from_dict = MessageMentionChannelResponse.from_dict(message_mention_channel_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


