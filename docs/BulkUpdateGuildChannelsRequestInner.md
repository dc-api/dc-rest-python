# BulkUpdateGuildChannelsRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**position** | **int** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**lock_permissions** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.bulk_update_guild_channels_request_inner import BulkUpdateGuildChannelsRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateGuildChannelsRequestInner from a JSON string
bulk_update_guild_channels_request_inner_instance = BulkUpdateGuildChannelsRequestInner.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateGuildChannelsRequestInner.to_json())

# convert the object into a dict
bulk_update_guild_channels_request_inner_dict = bulk_update_guild_channels_request_inner_instance.to_dict()
# create an instance of BulkUpdateGuildChannelsRequestInner from a dict
bulk_update_guild_channels_request_inner_from_dict = BulkUpdateGuildChannelsRequestInner.from_dict(bulk_update_guild_channels_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


