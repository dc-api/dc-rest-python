# WidgetChannel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**position** | **int** |  | 

## Example

```python
from dc_rest.models.widget_channel import WidgetChannel

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetChannel from a JSON string
widget_channel_instance = WidgetChannel.from_json(json)
# print the JSON string representation of the object
print(WidgetChannel.to_json())

# convert the object into a dict
widget_channel_dict = widget_channel_instance.to_dict()
# create an instance of WidgetChannel from a dict
widget_channel_from_dict = WidgetChannel.from_dict(widget_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


