# ApplicationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**icon** | **str** |  | [optional] 
**description** | **str** |  | 
**type** | **int** |  | [optional] 
**cover_image** | **str** |  | [optional] 
**primary_sku_id** | **str** |  | [optional] 
**bot** | [**UserResponse**](UserResponse.md) |  | [optional] 
**slug** | **str** |  | [optional] 
**guild_id** | **str** |  | [optional] 
**rpc_origins** | **List[Optional[str]]** |  | [optional] 
**bot_public** | **bool** |  | [optional] 
**bot_require_code_grant** | **bool** |  | [optional] 
**terms_of_service_url** | **str** |  | [optional] 
**privacy_policy_url** | **str** |  | [optional] 
**custom_install_url** | **str** |  | [optional] 
**install_params** | [**ApplicationOAuth2InstallParamsResponse**](ApplicationOAuth2InstallParamsResponse.md) |  | [optional] 
**integration_types_config** | [**Dict[str, ApplicationIntegrationTypeConfigurationResponse]**](ApplicationIntegrationTypeConfigurationResponse.md) |  | [optional] 
**verify_key** | **str** |  | 
**flags** | **int** |  | 
**max_participants** | **int** |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from dc_rest.models.application_response import ApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationResponse from a JSON string
application_response_instance = ApplicationResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationResponse.to_json())

# convert the object into a dict
application_response_dict = application_response_instance.to_dict()
# create an instance of ApplicationResponse from a dict
application_response_from_dict = ApplicationResponse.from_dict(application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


