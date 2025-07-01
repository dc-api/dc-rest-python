# ApplicationCommandOptionNumberChoiceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**name_localized** | **str** |  | [optional] 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**value** | **float** |  | 

## Example

```python
from dc_rest.models.application_command_option_number_choice_response import ApplicationCommandOptionNumberChoiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandOptionNumberChoiceResponse from a JSON string
application_command_option_number_choice_response_instance = ApplicationCommandOptionNumberChoiceResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandOptionNumberChoiceResponse.to_json())

# convert the object into a dict
application_command_option_number_choice_response_dict = application_command_option_number_choice_response_instance.to_dict()
# create an instance of ApplicationCommandOptionNumberChoiceResponse from a dict
application_command_option_number_choice_response_from_dict = ApplicationCommandOptionNumberChoiceResponse.from_dict(application_command_option_number_choice_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


