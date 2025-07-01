# ActionRowComponentResponseComponentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** |  | 
**id** | **int** |  | 
**custom_id** | **str** |  | 
**style** | **int** |  | 
**label** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**emoji** | [**ComponentEmojiResponse**](ComponentEmojiResponse.md) |  | [optional] 
**url** | **str** |  | [optional] 
**sku_id** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 
**min_values** | **int** |  | [optional] 
**max_values** | **int** |  | [optional] 
**channel_types** | **List[int]** |  | [optional] 
**default_values** | [**List[UserSelectDefaultValueResponse]**](UserSelectDefaultValueResponse.md) |  | [optional] 
**options** | [**List[StringSelectOptionResponse]**](StringSelectOptionResponse.md) |  | 
**value** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.action_row_component_response_components_inner import ActionRowComponentResponseComponentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActionRowComponentResponseComponentsInner from a JSON string
action_row_component_response_components_inner_instance = ActionRowComponentResponseComponentsInner.from_json(json)
# print the JSON string representation of the object
print(ActionRowComponentResponseComponentsInner.to_json())

# convert the object into a dict
action_row_component_response_components_inner_dict = action_row_component_response_components_inner_instance.to_dict()
# create an instance of ActionRowComponentResponseComponentsInner from a dict
action_row_component_response_components_inner_from_dict = ActionRowComponentResponseComponentsInner.from_dict(action_row_component_response_components_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


