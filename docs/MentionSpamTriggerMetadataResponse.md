# MentionSpamTriggerMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mention_total_limit** | **int** |  | 
**mention_raid_protection_enabled** | **bool** |  | [optional] 

## Example

```python
from dc_rest.models.mention_spam_trigger_metadata_response import MentionSpamTriggerMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MentionSpamTriggerMetadataResponse from a JSON string
mention_spam_trigger_metadata_response_instance = MentionSpamTriggerMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(MentionSpamTriggerMetadataResponse.to_json())

# convert the object into a dict
mention_spam_trigger_metadata_response_dict = mention_spam_trigger_metadata_response_instance.to_dict()
# create an instance of MentionSpamTriggerMetadataResponse from a dict
mention_spam_trigger_metadata_response_from_dict = MentionSpamTriggerMetadataResponse.from_dict(mention_spam_trigger_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


