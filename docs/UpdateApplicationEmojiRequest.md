# UpdateApplicationEmojiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_application_emoji_request import UpdateApplicationEmojiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateApplicationEmojiRequest from a JSON string
update_application_emoji_request_instance = UpdateApplicationEmojiRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateApplicationEmojiRequest.to_json())

# convert the object into a dict
update_application_emoji_request_dict = update_application_emoji_request_instance.to_dict()
# create an instance of UpdateApplicationEmojiRequest from a dict
update_application_emoji_request_from_dict = UpdateApplicationEmojiRequest.from_dict(update_application_emoji_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


