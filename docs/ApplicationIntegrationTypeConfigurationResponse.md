# ApplicationIntegrationTypeConfigurationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oauth2_install_params** | [**ApplicationOAuth2InstallParamsResponse**](ApplicationOAuth2InstallParamsResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.application_integration_type_configuration_response import ApplicationIntegrationTypeConfigurationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationIntegrationTypeConfigurationResponse from a JSON string
application_integration_type_configuration_response_instance = ApplicationIntegrationTypeConfigurationResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationIntegrationTypeConfigurationResponse.to_json())

# convert the object into a dict
application_integration_type_configuration_response_dict = application_integration_type_configuration_response_instance.to_dict()
# create an instance of ApplicationIntegrationTypeConfigurationResponse from a dict
application_integration_type_configuration_response_from_dict = ApplicationIntegrationTypeConfigurationResponse.from_dict(application_integration_type_configuration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


