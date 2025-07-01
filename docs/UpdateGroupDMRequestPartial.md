# UpdateGroupDMRequestPartial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**icon** | **str** |  | [optional] 

## Example

```python
from dc_rest.models.update_group_dm_request_partial import UpdateGroupDMRequestPartial

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupDMRequestPartial from a JSON string
update_group_dm_request_partial_instance = UpdateGroupDMRequestPartial.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupDMRequestPartial.to_json())

# convert the object into a dict
update_group_dm_request_partial_dict = update_group_dm_request_partial_instance.to_dict()
# create an instance of UpdateGroupDMRequestPartial from a dict
update_group_dm_request_partial_from_dict = UpdateGroupDMRequestPartial.from_dict(update_group_dm_request_partial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


