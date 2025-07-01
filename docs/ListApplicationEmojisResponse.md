# ListApplicationEmojisResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[EmojiResponse]**](EmojiResponse.md) |  | 

## Example

```python
from dc_rest.models.list_application_emojis_response import ListApplicationEmojisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListApplicationEmojisResponse from a JSON string
list_application_emojis_response_instance = ListApplicationEmojisResponse.from_json(json)
# print the JSON string representation of the object
print(ListApplicationEmojisResponse.to_json())

# convert the object into a dict
list_application_emojis_response_dict = list_application_emojis_response_instance.to_dict()
# create an instance of ListApplicationEmojisResponse from a dict
list_application_emojis_response_from_dict = ListApplicationEmojisResponse.from_dict(list_application_emojis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


