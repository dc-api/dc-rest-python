# MentionSpamTriggerMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mention_total_limit** | **int** |  | 
**mention_raid_protection_enabled** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.mention_spam_trigger_metadata import MentionSpamTriggerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of MentionSpamTriggerMetadata from a JSON string
mention_spam_trigger_metadata_instance = MentionSpamTriggerMetadata.from_json(json)
# print the JSON string representation of the object
print(MentionSpamTriggerMetadata.to_json())

# convert the object into a dict
mention_spam_trigger_metadata_dict = mention_spam_trigger_metadata_instance.to_dict()
# create an instance of MentionSpamTriggerMetadata from a dict
mention_spam_trigger_metadata_from_dict = MentionSpamTriggerMetadata.from_dict(mention_spam_trigger_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


