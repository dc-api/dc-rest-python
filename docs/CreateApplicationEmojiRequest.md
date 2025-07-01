# CreateApplicationEmojiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**image** | **str** |  | 

## Example

```python
from dc_rest.models.create_application_emoji_request import CreateApplicationEmojiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationEmojiRequest from a JSON string
create_application_emoji_request_instance = CreateApplicationEmojiRequest.from_json(json)
# print the JSON string representation of the object
print(CreateApplicationEmojiRequest.to_json())

# convert the object into a dict
create_application_emoji_request_dict = create_application_emoji_request_instance.to_dict()
# create an instance of CreateApplicationEmojiRequest from a dict
create_application_emoji_request_from_dict = CreateApplicationEmojiRequest.from_dict(create_application_emoji_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


