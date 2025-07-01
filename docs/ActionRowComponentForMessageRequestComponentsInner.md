# ActionRowComponentForMessageRequestComponentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**custom_id** | **str** |  | 
**style** | **int** |  | 
**label** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**sku_id** | **str** |  | [optional] 
**emoji** | [**ComponentEmojiForMessageRequest**](ComponentEmojiForMessageRequest.md) |  | [optional] 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**default_values** | [**List[UserSelectDefaultValue]**](UserSelectDefaultValue.md) |  | [optional] 
**channel_types** | **List[int]** |  | [optional] 
**options** | [**List[StringSelectOptionForMessageRequest]**](StringSelectOptionForMessageRequest.md) |  | 

## Example

```python
from dc_rest.models.action_row_component_for_message_request_components_inner import ActionRowComponentForMessageRequestComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRowComponentForMessageRequestComponentsInner from a JSON string
action_row_component_for_message_request_components_inner_instance = ActionRowComponentForMessageRequestComponentsInner.from_json(json)
# print the JSON string representation of the object
print(ActionRowComponentForMessageRequestComponentsInner.to_json())

# convert the object into a dict
action_row_component_for_message_request_components_inner_dict = action_row_component_for_message_request_components_inner_instance.to_dict()
# create an instance of ActionRowComponentForMessageRequestComponentsInner from a dict
action_row_component_for_message_request_components_inner_from_dict = ActionRowComponentForMessageRequestComponentsInner.from_dict(action_row_component_for_message_request_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


