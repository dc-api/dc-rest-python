# ApplicationIntegrationTypeConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oauth2_install_params** | [**ApplicationOAuth2InstallParams**](ApplicationOAuth2InstallParams.md) |  | [optional] 

## Example

```python
from dc_rest.models.application_integration_type_configuration import ApplicationIntegrationTypeConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationIntegrationTypeConfiguration from a JSON string
application_integration_type_configuration_instance = ApplicationIntegrationTypeConfiguration.from_json(json)
# print the JSON string representation of the object
print(ApplicationIntegrationTypeConfiguration.to_json())

# convert the object into a dict
application_integration_type_configuration_dict = application_integration_type_configuration_instance.to_dict()
# create an instance of ApplicationIntegrationTypeConfiguration from a dict
application_integration_type_configuration_from_dict = ApplicationIntegrationTypeConfiguration.from_dict(application_integration_type_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


