# IntegrationApplicationResponse


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

## Example

```python
from dc_rest.models.integration_application_response import IntegrationApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationApplicationResponse from a JSON string
integration_application_response_instance = IntegrationApplicationResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationApplicationResponse.to_json())

# convert the object into a dict
integration_application_response_dict = integration_application_response_instance.to_dict()
# create an instance of IntegrationApplicationResponse from a dict
integration_application_response_from_dict = IntegrationApplicationResponse.from_dict(integration_application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


