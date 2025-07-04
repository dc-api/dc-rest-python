# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-05T02:42:22.742560433Z[Etc/UTC]
- **Generator Version**: 7.14.0

<details>
<summary><strong>⚠️ Important Disclaimer & Limitation of Liability</strong></summary>
<br>
> **IMPORTANT**: This software is provided "as is" without any warranties, express or implied, including but not limited
> to warranties of merchantability, fitness for a particular purpose, or non-infringement. The developers, contributors,
> and licensors (collectively, "Developers") make no representations regarding the accuracy, completeness, or reliability
> of this software or its outputs.
>
> This client is not intended to provide financial, investment, tax, or legal advice. It facilitates interaction with the
> Discord HTTP API (Preview) service but does not endorse or recommend any financial actions, including the purchase, sale, or holding of
> financial instruments (e.g., stocks, bonds, derivatives, cryptocurrencies). Users must consult qualified financial or
> legal professionals before making decisions based on this software's outputs.
>
> Financial markets are inherently speculative and carry significant risks. Using this software in trading, analysis, or
> other financial activities may result in substantial losses, including total loss of capital. The Developers are not
> liable for any losses or damages arising from such use. Users assume full responsibility for validating the software's
> outputs and ensuring their suitability for intended purposes.
>
> This client may rely on third-party data or services (e.g., market feeds, APIs). The Developers do not control or verify
> the accuracy of these services and are not liable for any errors, delays, or losses resulting from their use. Users must
> comply with third-party terms and conditions.
>
> Users are solely responsible for ensuring compliance with all applicable financial, tax, and regulatory requirements in
> their jurisdiction. This includes obtaining necessary licenses or approvals for trading or investment activities. The
> Developers disclaim liability for any legal consequences arising from non-compliance.
>
> To the fullest extent permitted by law, the Developers shall not be liable for any direct, indirect, incidental,
> consequential, or punitive damages arising from the use or inability to use this software, including but not limited to
> loss of profits, data, or business opportunities.

</details>
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.github_check_run import GithubCheckRun
from dc_rest.models.github_check_suite import GithubCheckSuite
from dc_rest.models.github_comment import GithubComment
from dc_rest.models.github_commit import GithubCommit
from dc_rest.models.github_discussion import GithubDiscussion
from dc_rest.models.github_issue import GithubIssue
from dc_rest.models.github_release import GithubRelease
from dc_rest.models.github_repository import GithubRepository
from dc_rest.models.github_review import GithubReview
from dc_rest.models.github_user import GithubUser
from typing import Optional, Set
from typing_extensions import Self

class GithubWebhook(BaseModel):
    """
    GithubWebhook
    """ # noqa: E501
    action: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    ref: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    ref_type: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    comment: Optional[GithubComment] = None
    issue: Optional[GithubIssue] = None
    pull_request: Optional[GithubIssue] = None
    repository: Optional[GithubRepository] = None
    forkee: Optional[GithubRepository] = None
    sender: GithubUser
    member: Optional[GithubUser] = None
    release: Optional[GithubRelease] = None
    head_commit: Optional[GithubCommit] = None
    commits: Optional[Annotated[List[GithubCommit], Field(max_length=1521)]] = None
    forced: Optional[StrictBool] = None
    compare: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    review: Optional[GithubReview] = None
    check_run: Optional[GithubCheckRun] = None
    check_suite: Optional[GithubCheckSuite] = None
    discussion: Optional[GithubDiscussion] = None
    answer: Optional[GithubComment] = None
    __properties: ClassVar[List[str]] = ["action", "ref", "ref_type", "comment", "issue", "pull_request", "repository", "forkee", "sender", "member", "release", "head_commit", "commits", "forced", "compare", "review", "check_run", "check_suite", "discussion", "answer"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GithubWebhook from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict['comment'] = self.comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of issue
        if self.issue:
            _dict['issue'] = self.issue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pull_request
        if self.pull_request:
            _dict['pull_request'] = self.pull_request.to_dict()
        # override the default output from pydantic by calling `to_dict()` of repository
        if self.repository:
            _dict['repository'] = self.repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of forkee
        if self.forkee:
            _dict['forkee'] = self.forkee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sender
        if self.sender:
            _dict['sender'] = self.sender.to_dict()
        # override the default output from pydantic by calling `to_dict()` of member
        if self.member:
            _dict['member'] = self.member.to_dict()
        # override the default output from pydantic by calling `to_dict()` of release
        if self.release:
            _dict['release'] = self.release.to_dict()
        # override the default output from pydantic by calling `to_dict()` of head_commit
        if self.head_commit:
            _dict['head_commit'] = self.head_commit.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in commits (list)
        _items = []
        if self.commits:
            for _item_commits in self.commits:
                if _item_commits:
                    _items.append(_item_commits.to_dict())
            _dict['commits'] = _items
        # override the default output from pydantic by calling `to_dict()` of review
        if self.review:
            _dict['review'] = self.review.to_dict()
        # override the default output from pydantic by calling `to_dict()` of check_run
        if self.check_run:
            _dict['check_run'] = self.check_run.to_dict()
        # override the default output from pydantic by calling `to_dict()` of check_suite
        if self.check_suite:
            _dict['check_suite'] = self.check_suite.to_dict()
        # override the default output from pydantic by calling `to_dict()` of discussion
        if self.discussion:
            _dict['discussion'] = self.discussion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of answer
        if self.answer:
            _dict['answer'] = self.answer.to_dict()
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if ref (nullable) is None
        # and model_fields_set contains the field
        if self.ref is None and "ref" in self.model_fields_set:
            _dict['ref'] = None

        # set to None if ref_type (nullable) is None
        # and model_fields_set contains the field
        if self.ref_type is None and "ref_type" in self.model_fields_set:
            _dict['ref_type'] = None

        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if issue (nullable) is None
        # and model_fields_set contains the field
        if self.issue is None and "issue" in self.model_fields_set:
            _dict['issue'] = None

        # set to None if pull_request (nullable) is None
        # and model_fields_set contains the field
        if self.pull_request is None and "pull_request" in self.model_fields_set:
            _dict['pull_request'] = None

        # set to None if repository (nullable) is None
        # and model_fields_set contains the field
        if self.repository is None and "repository" in self.model_fields_set:
            _dict['repository'] = None

        # set to None if forkee (nullable) is None
        # and model_fields_set contains the field
        if self.forkee is None and "forkee" in self.model_fields_set:
            _dict['forkee'] = None

        # set to None if member (nullable) is None
        # and model_fields_set contains the field
        if self.member is None and "member" in self.model_fields_set:
            _dict['member'] = None

        # set to None if release (nullable) is None
        # and model_fields_set contains the field
        if self.release is None and "release" in self.model_fields_set:
            _dict['release'] = None

        # set to None if head_commit (nullable) is None
        # and model_fields_set contains the field
        if self.head_commit is None and "head_commit" in self.model_fields_set:
            _dict['head_commit'] = None

        # set to None if commits (nullable) is None
        # and model_fields_set contains the field
        if self.commits is None and "commits" in self.model_fields_set:
            _dict['commits'] = None

        # set to None if forced (nullable) is None
        # and model_fields_set contains the field
        if self.forced is None and "forced" in self.model_fields_set:
            _dict['forced'] = None

        # set to None if compare (nullable) is None
        # and model_fields_set contains the field
        if self.compare is None and "compare" in self.model_fields_set:
            _dict['compare'] = None

        # set to None if review (nullable) is None
        # and model_fields_set contains the field
        if self.review is None and "review" in self.model_fields_set:
            _dict['review'] = None

        # set to None if check_run (nullable) is None
        # and model_fields_set contains the field
        if self.check_run is None and "check_run" in self.model_fields_set:
            _dict['check_run'] = None

        # set to None if check_suite (nullable) is None
        # and model_fields_set contains the field
        if self.check_suite is None and "check_suite" in self.model_fields_set:
            _dict['check_suite'] = None

        # set to None if discussion (nullable) is None
        # and model_fields_set contains the field
        if self.discussion is None and "discussion" in self.model_fields_set:
            _dict['discussion'] = None

        # set to None if answer (nullable) is None
        # and model_fields_set contains the field
        if self.answer is None and "answer" in self.model_fields_set:
            _dict['answer'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GithubWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GithubWebhook) in the input: " + _key)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "ref": obj.get("ref"),
            "ref_type": obj.get("ref_type"),
            "comment": GithubComment.from_dict(obj["comment"]) if obj.get("comment") is not None else None,
            "issue": GithubIssue.from_dict(obj["issue"]) if obj.get("issue") is not None else None,
            "pull_request": GithubIssue.from_dict(obj["pull_request"]) if obj.get("pull_request") is not None else None,
            "repository": GithubRepository.from_dict(obj["repository"]) if obj.get("repository") is not None else None,
            "forkee": GithubRepository.from_dict(obj["forkee"]) if obj.get("forkee") is not None else None,
            "sender": GithubUser.from_dict(obj["sender"]) if obj.get("sender") is not None else None,
            "member": GithubUser.from_dict(obj["member"]) if obj.get("member") is not None else None,
            "release": GithubRelease.from_dict(obj["release"]) if obj.get("release") is not None else None,
            "head_commit": GithubCommit.from_dict(obj["head_commit"]) if obj.get("head_commit") is not None else None,
            "commits": [GithubCommit.from_dict(_item) for _item in obj["commits"]] if obj.get("commits") is not None else None,
            "forced": obj.get("forced"),
            "compare": obj.get("compare"),
            "review": GithubReview.from_dict(obj["review"]) if obj.get("review") is not None else None,
            "check_run": GithubCheckRun.from_dict(obj["check_run"]) if obj.get("check_run") is not None else None,
            "check_suite": GithubCheckSuite.from_dict(obj["check_suite"]) if obj.get("check_suite") is not None else None,
            "discussion": GithubDiscussion.from_dict(obj["discussion"]) if obj.get("discussion") is not None else None,
            "answer": GithubComment.from_dict(obj["answer"]) if obj.get("answer") is not None else None
        })
        return _obj


