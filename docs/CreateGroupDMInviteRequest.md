# CreateGroupDMInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_age** | **int** |  | [optional] 

## Example

```python
from dc_rest.models.create_group_dm_invite_request import CreateGroupDMInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupDMInviteRequest from a JSON string
create_group_dm_invite_request_instance = CreateGroupDMInviteRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGroupDMInviteRequest.to_json())

# convert the object into a dict
create_group_dm_invite_request_dict = create_group_dm_invite_request_instance.to_dict()
# create an instance of CreateGroupDMInviteRequest from a dict
create_group_dm_invite_request_from_dict = CreateGroupDMInviteRequest.from_dict(create_group_dm_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


