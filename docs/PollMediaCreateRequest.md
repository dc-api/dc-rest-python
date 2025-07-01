# PollMediaCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**emoji** | [**PollEmojiCreateRequest**](PollEmojiCreateRequest.md) |  | [optional] 

## Example

```python
from dc_rest.models.poll_media_create_request import PollMediaCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PollMediaCreateRequest from a JSON string
poll_media_create_request_instance = PollMediaCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PollMediaCreateRequest.to_json())

# convert the object into a dict
poll_media_create_request_dict = poll_media_create_request_instance.to_dict()
# create an instance of PollMediaCreateRequest from a dict
poll_media_create_request_from_dict = PollMediaCreateRequest.from_dict(poll_media_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


