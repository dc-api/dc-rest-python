# ContainerComponentForMessageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**accent_color** | **int** |  | [optional] 
**components** | [**List[ContainerComponentForMessageRequestComponentsInner]**](ContainerComponentForMessageRequestComponentsInner.md) |  | 
**spoiler** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.container_component_for_message_request import ContainerComponentForMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerComponentForMessageRequest from a JSON string
container_component_for_message_request_instance = ContainerComponentForMessageRequest.from_json(json)
# print the JSON string representation of the object
print(ContainerComponentForMessageRequest.to_json())

# convert the object into a dict
container_component_for_message_request_dict = container_component_for_message_request_instance.to_dict()
# create an instance of ContainerComponentForMessageRequest from a dict
container_component_for_message_request_from_dict = ContainerComponentForMessageRequest.from_dict(container_component_for_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


