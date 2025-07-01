# StageInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guild_id** | **str** |  | 
**channel_id** | **str** |  | 
**topic** | **str** |  | 
**privacy_level** | **int** |  | 
**id** | **str** |  | 
**discoverable_disabled** | **bool** |  | [optional] 
**guild_scheduled_event_id** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.stage_instance_response import StageInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StageInstanceResponse from a JSON string
stage_instance_response_instance = StageInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(StageInstanceResponse.to_json())

# convert the object into a dict
stage_instance_response_dict = stage_instance_response_instance.to_dict()
# create an instance of StageInstanceResponse from a dict
stage_instance_response_from_dict = StageInstanceResponse.from_dict(stage_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


