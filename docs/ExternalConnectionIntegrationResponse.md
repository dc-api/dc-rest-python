# ExternalConnectionIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**account** | [**AccountResponse**](AccountResponse.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**id** | **str** |  | 
**user** | [**UserResponse**](UserResponse.md) |  | 
**revoked** | **bool** |  | [optional] 
**expire_behavior** | **int** |  | [optional] 
**expire_grace_period** | **int** |  | [optional] 
**subscriber_count** | **int** |  | [optional] 
**synced_at** | **datetime** |  | [optional] 
**role_id** | **str** |  | [optional] 
**syncing** | **bool** |  | [optional] 
**enable_emoticons** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.external_connection_integration_response import ExternalConnectionIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalConnectionIntegrationResponse from a JSON string
external_connection_integration_response_instance = ExternalConnectionIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(ExternalConnectionIntegrationResponse.to_json())

# convert the object into a dict
external_connection_integration_response_dict = external_connection_integration_response_instance.to_dict()
# create an instance of ExternalConnectionIntegrationResponse from a dict
external_connection_integration_response_from_dict = ExternalConnectionIntegrationResponse.from_dict(external_connection_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


