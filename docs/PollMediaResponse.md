# PollMediaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**emoji** | [**MessageReactionEmojiResponse**](MessageReactionEmojiResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.poll_media_response import PollMediaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PollMediaResponse from a JSON string
poll_media_response_instance = PollMediaResponse.from_json(json)
# print the JSON string representation of the object
print(PollMediaResponse.to_json())

# convert the object into a dict
poll_media_response_dict = poll_media_response_instance.to_dict()
# create an instance of PollMediaResponse from a dict
poll_media_response_from_dict = PollMediaResponse.from_dict(poll_media_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


