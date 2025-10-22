# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.course_lesson_interaction import CourseLessonInteraction

__all__ = ["CourseLessonInteractionCompletedWebhookEvent"]


class CourseLessonInteractionCompletedWebhookEvent(BaseModel):
    id: str
    """A unique ID for every single webhook request"""

    api_version: Literal["v1"]
    """The API version for this webhook"""

    data: CourseLessonInteraction
    """A lesson interaction tracking user progress in courses"""

    timestamp: datetime
    """The timestamp in ISO 8601 format that the webhook was sent at on the server"""

    type: Literal["course_lesson_interaction.completed"]
    """The webhook event type"""
