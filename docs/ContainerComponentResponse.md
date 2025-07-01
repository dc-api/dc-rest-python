# ContainerComponentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**accent_color** | **int** |  | [optional] 
**components** | [**List[ContainerComponentResponseComponentsInner]**](ContainerComponentResponseComponentsInner.md) |  | 
**spoiler** | **bool** |  | 

## Example

```python
from dc_rest.models.container_component_response import ContainerComponentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerComponentResponse from a JSON string
container_component_response_instance = ContainerComponentResponse.from_json(json)
# print the JSON string representation of the object
print(ContainerComponentResponse.to_json())

# convert the object into a dict
container_component_response_dict = container_component_response_instance.to_dict()
# create an instance of ContainerComponentResponse from a dict
container_component_response_from_dict = ContainerComponentResponse.from_dict(container_component_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


