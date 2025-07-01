# BaseCreateMessageCreateRequestComponentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**components** | [**List[TextDisplayComponentForMessageRequest]**](TextDisplayComponentForMessageRequest.md) |  | 
**accent_color** | **int** |  | [optional] 
**spoiler** | **bool** |  | [optional] 
**file** | [**UnfurledMediaRequestWithAttachmentReferenceRequired**](UnfurledMediaRequestWithAttachmentReferenceRequired.md) |  | 
**items** | [**List[MediaGalleryItemRequest]**](MediaGalleryItemRequest.md) |  | 
**accessory** | [**SectionComponentForMessageRequestAccessory**](SectionComponentForMessageRequestAccessory.md) |  | 
**spacing** | **int** |  | [optional] 
**divider** | **bool** |  | [optional] 
**content** | **str** |  | 

## Example

```python
from dc_rest.models.base_create_message_create_request_components_inner import BaseCreateMessageCreateRequestComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BaseCreateMessageCreateRequestComponentsInner from a JSON string
base_create_message_create_request_components_inner_instance = BaseCreateMessageCreateRequestComponentsInner.from_json(json)
# print the JSON string representation of the object
print(BaseCreateMessageCreateRequestComponentsInner.to_json())

# convert the object into a dict
base_create_message_create_request_components_inner_dict = base_create_message_create_request_components_inner_instance.to_dict()
# create an instance of BaseCreateMessageCreateRequestComponentsInner from a dict
base_create_message_create_request_components_inner_from_dict = BaseCreateMessageCreateRequestComponentsInner.from_dict(base_create_message_create_request_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


