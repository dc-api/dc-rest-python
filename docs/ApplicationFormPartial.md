# ApplicationFormPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**ApplicationFormPartialDescription**](ApplicationFormPartialDescription.md) |  | [optional] 
**icon** | **str** |  | [optional] 
**cover_image** | **str** |  | [optional] 
**team_id** | **str** |  | [optional] 
**flags** | **int** |  | [optional] 
**interactions_endpoint_url** | **str** |  | [optional] 
**explicit_content_filter** | **int** |  | [optional] 
**max_participants** | **int** |  | [optional] 
**type** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**custom_install_url** | **str** |  | [optional] 
**install_params** | [**ApplicationOAuth2InstallParams**](ApplicationOAuth2InstallParams.md) |  | [optional] 
**role_connections_verification_url** | **str** |  | [optional] 
**integration_types_config** | [**Dict[str, ApplicationFormPartialIntegrationTypesConfigValue]**](ApplicationFormPartialIntegrationTypesConfigValue.md) |  | [optional] 

## Example

```python
from dc_rest.models.application_form_partial import ApplicationFormPartial

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFormPartial from a JSON string
application_form_partial_instance = ApplicationFormPartial.from_json(json)
# print the JSON string representation of the object
print(ApplicationFormPartial.to_json())

# convert the object into a dict
application_form_partial_dict = application_form_partial_instance.to_dict()
# create an instance of ApplicationFormPartial from a dict
application_form_partial_from_dict = ApplicationFormPartial.from_dict(application_form_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


