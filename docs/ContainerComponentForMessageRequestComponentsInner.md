# ContainerComponentForMessageRequestComponentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**components** | [**List[TextDisplayComponentForMessageRequest]**](TextDisplayComponentForMessageRequest.md) |  | 
**spoiler** | **bool** |  | [optional] 
**file** | [**UnfurledMediaRequestWithAttachmentReferenceRequired**](UnfurledMediaRequestWithAttachmentReferenceRequired.md) |  | 
**items** | [**List[MediaGalleryItemRequest]**](MediaGalleryItemRequest.md) |  | 
**accessory** | [**SectionComponentForMessageRequestAccessory**](SectionComponentForMessageRequestAccessory.md) |  | 
**spacing** | **int** |  | [optional] 
**divider** | **bool** |  | [optional] 
**content** | **str** |  | 

## Example

```python
from dc_rest.models.container_component_for_message_request_components_inner import ContainerComponentForMessageRequestComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerComponentForMessageRequestComponentsInner from a JSON string
container_component_for_message_request_components_inner_instance = ContainerComponentForMessageRequestComponentsInner.from_json(json)
# print the JSON string representation of the object
print(ContainerComponentForMessageRequestComponentsInner.to_json())

# convert the object into a dict
container_component_for_message_request_components_inner_dict = container_component_for_message_request_components_inner_instance.to_dict()
# create an instance of ContainerComponentForMessageRequestComponentsInner from a dict
container_component_for_message_request_components_inner_from_dict = ContainerComponentForMessageRequestComponentsInner.from_dict(container_component_for_message_request_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


