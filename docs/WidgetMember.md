# WidgetMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**username** | **str** |  | 
**discriminator** | **str** |  | 
**avatar** | **object** |  | [optional] 
**status** | **str** |  | 
**avatar_url** | **str** |  | 
**activity** | [**WidgetActivity**](WidgetActivity.md) |  | [optional] 
**deaf** | **bool** |  | [optional] 
**mute** | **bool** |  | [optional] 
**self_deaf** | **bool** |  | [optional] 
**self_mute** | **bool** |  | [optional] 
**suppress** | **bool** |  | [optional] 
**channel_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.widget_member import WidgetMember

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetMember from a JSON string
widget_member_instance = WidgetMember.from_json(json)
# print the JSON string representation of the object
print(WidgetMember.to_json())

# convert the object into a dict
widget_member_dict = widget_member_instance.to_dict()
# create an instance of WidgetMember from a dict
widget_member_from_dict = WidgetMember.from_dict(widget_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


