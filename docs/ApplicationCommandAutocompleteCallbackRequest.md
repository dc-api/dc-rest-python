# ApplicationCommandAutocompleteCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**data** | [**ApplicationCommandAutocompleteCallbackRequestData**](ApplicationCommandAutocompleteCallbackRequestData.md) |  | 

## Example

```python
from dc_rest.models.application_command_autocomplete_callback_request import ApplicationCommandAutocompleteCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandAutocompleteCallbackRequest from a JSON string
application_command_autocomplete_callback_request_instance = ApplicationCommandAutocompleteCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandAutocompleteCallbackRequest.to_json())

# convert the object into a dict
application_command_autocomplete_callback_request_dict = application_command_autocomplete_callback_request_instance.to_dict()
# create an instance of ApplicationCommandAutocompleteCallbackRequest from a dict
application_command_autocomplete_callback_request_from_dict = ApplicationCommandAutocompleteCallbackRequest.from_dict(application_command_autocomplete_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


