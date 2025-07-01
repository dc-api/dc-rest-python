# WelcomeMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_ids** | **List[str]** |  | 
**message** | **str** |  | 

## Example

```python
from dc_rest.models.welcome_message_response import WelcomeMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WelcomeMessageResponse from a JSON string
welcome_message_response_instance = WelcomeMessageResponse.from_json(json)
# print the JSON string representation of the object
print(WelcomeMessageResponse.to_json())

# convert the object into a dict
welcome_message_response_dict = welcome_message_response_instance.to_dict()
# create an instance of WelcomeMessageResponse from a dict
welcome_message_response_from_dict = WelcomeMessageResponse.from_dict(welcome_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


