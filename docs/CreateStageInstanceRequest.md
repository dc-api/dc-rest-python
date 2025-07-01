# CreateStageInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** |  | 
**channel_id** | **str** |  | 
**privacy_level** | **int** |  | [optional] 
**guild_scheduled_event_id** | **str** |  | [optional] 
**send_start_notification** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.create_stage_instance_request import CreateStageInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStageInstanceRequest from a JSON string
create_stage_instance_request_instance = CreateStageInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(CreateStageInstanceRequest.to_json())

# convert the object into a dict
create_stage_instance_request_dict = create_stage_instance_request_instance.to_dict()
# create an instance of CreateStageInstanceRequest from a dict
create_stage_instance_request_from_dict = CreateStageInstanceRequest.from_dict(create_stage_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


