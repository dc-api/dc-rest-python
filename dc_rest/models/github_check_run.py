# coding: utf-8

"""
Discord HTTP API (Preview) - REST API Client
Preview of the Discord v10 HTTP API specification. See https://discord.com/developers/docs for more details.

## Metadata

- **Copyright**: Copyright (c) 2025 Qntx
- **Author**: ΣX <gitctrlx@gmail.com>
- **Version**: 10
- **Modified**: 2025-07-01T10:27:27.208780920Z[Etc/UTC]
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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dc_rest.models.github_check_pull_request import GithubCheckPullRequest
from dc_rest.models.github_check_run_output import GithubCheckRunOutput
from dc_rest.models.github_check_suite import GithubCheckSuite
from typing import Optional, Set
from typing_extensions import Self

class GithubCheckRun(BaseModel):
    """
    GithubCheckRun
    """ # noqa: E501
    conclusion: Optional[Annotated[str, Field(strict=True, max_length=152133)]] = None
    name: Annotated[str, Field(strict=True, max_length=152133)]
    html_url: Annotated[str, Field(strict=True, max_length=2048)]
    check_suite: GithubCheckSuite
    details_url: Optional[Annotated[str, Field(strict=True, max_length=2048)]] = None
    output: Optional[GithubCheckRunOutput] = None
    pull_requests: Optional[Annotated[List[GithubCheckPullRequest], Field(max_length=1521)]] = None
    __properties: ClassVar[List[str]] = ["conclusion", "name", "html_url", "check_suite", "details_url", "output", "pull_requests"]

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
        """Create an instance of GithubCheckRun from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of check_suite
        if self.check_suite:
            _dict['check_suite'] = self.check_suite.to_dict()
        # override the default output from pydantic by calling `to_dict()` of output
        if self.output:
            _dict['output'] = self.output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in pull_requests (list)
        _items = []
        if self.pull_requests:
            for _item_pull_requests in self.pull_requests:
                if _item_pull_requests:
                    _items.append(_item_pull_requests.to_dict())
            _dict['pull_requests'] = _items
        # set to None if conclusion (nullable) is None
        # and model_fields_set contains the field
        if self.conclusion is None and "conclusion" in self.model_fields_set:
            _dict['conclusion'] = None

        # set to None if details_url (nullable) is None
        # and model_fields_set contains the field
        if self.details_url is None and "details_url" in self.model_fields_set:
            _dict['details_url'] = None

        # set to None if output (nullable) is None
        # and model_fields_set contains the field
        if self.output is None and "output" in self.model_fields_set:
            _dict['output'] = None

        # set to None if pull_requests (nullable) is None
        # and model_fields_set contains the field
        if self.pull_requests is None and "pull_requests" in self.model_fields_set:
            _dict['pull_requests'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GithubCheckRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in GithubCheckRun) in the input: " + _key)

        _obj = cls.model_validate({
            "conclusion": obj.get("conclusion"),
            "name": obj.get("name"),
            "html_url": obj.get("html_url"),
            "check_suite": GithubCheckSuite.from_dict(obj["check_suite"]) if obj.get("check_suite") is not None else None,
            "details_url": obj.get("details_url"),
            "output": GithubCheckRunOutput.from_dict(obj["output"]) if obj.get("output") is not None else None,
            "pull_requests": [GithubCheckPullRequest.from_dict(_item) for _item in obj["pull_requests"]] if obj.get("pull_requests") is not None else None
        })
        return _obj


