# PartialExternalConnectionIntegrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**name** | **str** |  | [optional] 
**account** | [**AccountResponse**](AccountResponse.md) |  | [optional] 

## Example

```python
from dc_rest.models.partial_external_connection_integration_response import PartialExternalConnectionIntegrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PartialExternalConnectionIntegrationResponse from a JSON string
partial_external_connection_integration_response_instance = PartialExternalConnectionIntegrationResponse.from_json(json)
# print the JSON string representation of the object
print(PartialExternalConnectionIntegrationResponse.to_json())

# convert the object into a dict
partial_external_connection_integration_response_dict = partial_external_connection_integration_response_instance.to_dict()
# create an instance of PartialExternalConnectionIntegrationResponse from a dict
partial_external_connection_integration_response_from_dict = PartialExternalConnectionIntegrationResponse.from_dict(partial_external_connection_integration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


