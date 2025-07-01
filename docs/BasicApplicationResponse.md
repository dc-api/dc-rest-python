# BasicApplicationResponse


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
from dc_rest.models.basic_application_response import BasicApplicationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BasicApplicationResponse from a JSON string
basic_application_response_instance = BasicApplicationResponse.from_json(json)
# print the JSON string representation of the object
print(BasicApplicationResponse.to_json())

# convert the object into a dict
basic_application_response_dict = basic_application_response_instance.to_dict()
# create an instance of BasicApplicationResponse from a dict
basic_application_response_from_dict = BasicApplicationResponse.from_dict(basic_application_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


