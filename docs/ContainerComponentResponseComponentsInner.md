# ContainerComponentResponseComponentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**components** | [**List[TextDisplayComponentResponse]**](TextDisplayComponentResponse.md) |  | 
**file** | [**UnfurledMediaResponse**](UnfurledMediaResponse.md) |  | 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**spoiler** | **bool** |  | 
**items** | [**List[MediaGalleryItemResponse]**](MediaGalleryItemResponse.md) |  | 
**accessory** | [**SectionComponentResponseAccessory**](SectionComponentResponseAccessory.md) |  | 
**spacing** | **int** |  | 
**divider** | **bool** |  | 
**content** | **str** |  | 

## Example

```python
from dc_rest.models.container_component_response_components_inner import ContainerComponentResponseComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerComponentResponseComponentsInner from a JSON string
container_component_response_components_inner_instance = ContainerComponentResponseComponentsInner.from_json(json)
# print the JSON string representation of the object
print(ContainerComponentResponseComponentsInner.to_json())

# convert the object into a dict
container_component_response_components_inner_dict = container_component_response_components_inner_instance.to_dict()
# create an instance of ContainerComponentResponseComponentsInner from a dict
container_component_response_components_inner_from_dict = ContainerComponentResponseComponentsInner.from_dict(container_component_response_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


