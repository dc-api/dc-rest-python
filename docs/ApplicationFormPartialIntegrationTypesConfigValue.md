# ApplicationFormPartialIntegrationTypesConfigValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oauth2_install_params** | [**ApplicationOAuth2InstallParams**](ApplicationOAuth2InstallParams.md) |  | [optional] 

## Example

```python
from dc_rest.models.application_form_partial_integration_types_config_value import ApplicationFormPartialIntegrationTypesConfigValue

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFormPartialIntegrationTypesConfigValue from a JSON string
application_form_partial_integration_types_config_value_instance = ApplicationFormPartialIntegrationTypesConfigValue.from_json(json)
# print the JSON string representation of the object
print(ApplicationFormPartialIntegrationTypesConfigValue.to_json())

# convert the object into a dict
application_form_partial_integration_types_config_value_dict = application_form_partial_integration_types_config_value_instance.to_dict()
# create an instance of ApplicationFormPartialIntegrationTypesConfigValue from a dict
application_form_partial_integration_types_config_value_from_dict = ApplicationFormPartialIntegrationTypesConfigValue.from_dict(application_form_partial_integration_types_config_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


