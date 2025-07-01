# UpdateStageInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** |  | [optional] 
**privacy_level** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.update_stage_instance_request import UpdateStageInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStageInstanceRequest from a JSON string
update_stage_instance_request_instance = UpdateStageInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateStageInstanceRequest.to_json())

# convert the object into a dict
update_stage_instance_request_dict = update_stage_instance_request_instance.to_dict()
# create an instance of UpdateStageInstanceRequest from a dict
update_stage_instance_request_from_dict = UpdateStageInstanceRequest.from_dict(update_stage_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


