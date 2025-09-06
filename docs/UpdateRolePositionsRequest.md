# UpdateRolePositionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**position** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.update_role_positions_request import UpdateRolePositionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRolePositionsRequest from a JSON string
update_role_positions_request_instance = UpdateRolePositionsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRolePositionsRequest.to_json())

# convert the object into a dict
update_role_positions_request_dict = update_role_positions_request_instance.to_dict()
# create an instance of UpdateRolePositionsRequest from a dict
update_role_positions_request_from_dict = UpdateRolePositionsRequest.from_dict(update_role_positions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


