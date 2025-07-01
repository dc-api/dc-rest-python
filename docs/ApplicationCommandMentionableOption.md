# ApplicationCommandMentionableOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**name** | **str** |  | 
**name_localizations** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | 
**description_localizations** | **Dict[str, str]** |  | [optional] 
**required** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.application_command_mentionable_option import ApplicationCommandMentionableOption

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCommandMentionableOption from a JSON string
application_command_mentionable_option_instance = ApplicationCommandMentionableOption.from_json(json)
# print the JSON string representation of the object
print(ApplicationCommandMentionableOption.to_json())

# convert the object into a dict
application_command_mentionable_option_dict = application_command_mentionable_option_instance.to_dict()
# create an instance of ApplicationCommandMentionableOption from a dict
application_command_mentionable_option_from_dict = ApplicationCommandMentionableOption.from_dict(application_command_mentionable_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


