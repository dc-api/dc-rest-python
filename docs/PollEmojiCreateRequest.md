# PollEmojiCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**animated** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.poll_emoji_create_request import PollEmojiCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PollEmojiCreateRequest from a JSON string
poll_emoji_create_request_instance = PollEmojiCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PollEmojiCreateRequest.to_json())

# convert the object into a dict
poll_emoji_create_request_dict = poll_emoji_create_request_instance.to_dict()
# create an instance of PollEmojiCreateRequest from a dict
poll_emoji_create_request_from_dict = PollEmojiCreateRequest.from_dict(poll_emoji_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


