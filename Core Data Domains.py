from dataclass import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional, List, Dict, Any
from decimal import Decimal
import json
import uuid

class EventType(Enum):
    PLAY_Start = "play_start"
    PLAY_PAUSE = "play_pause"
    PLAY_RESUME = "play_resume"
    PLAY_STOP = "play_stop"
    PLAY_COMPLETE = "play_complete"
    SEEK = "seek"
    SEARCH = "search"
    BROWSE = "browse"
    CLICK = "click"
    SCROLL = "scroll"
    ADD_TO_LIST = "add_to_list"
    REMOVE_FROM_LIST = "remove_from_list"
    RATE_CONTENT = "rate_content"
    SHARE = "share"
    
class DeviceType(Enum):
    MOBILE_IOS = "mobile_ios"
    MOBILE_ANDROID = "mobile_android"
    WEB_DESKTOP = "web_desktop"
    WEB_MOBILE = "web_mobile"
    TV_SMART_TV = "tv_streaming_device"
    GAME_CONSOLE = "game_console"
    TABLET = "tablet"
    
class ContentType(Enum):
    MOVIE = "movie"
    TV_SERIES = "tv_series"
    TV_EPISODE = "tv_episdoe"
    DOCUMENTARY = "documentary"
    SHORT_FORM = "short_form"
    LIVE_EVENT = "live_event"
    TRAILER = "trailer"
    
class MaturityRating(Enum):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"
    TV_Y = "TV-Y"
    TV_Y7 = "TV-Y7"
    TV_G = "TV-G"
    TV_PG = "TV-PG"
    TV_14 = "TV-14"
    TV_MA = "TV-MA"
    
Class SubscriptionTier(Enum):
    FREE = "free"
    BASIC = "basic"
    STANDARD = "standard"
    PREMIUM = "premium"
    FAMILY = "family"
    
class SubscriptionStatus(Enum):
    ACTIVE = "active"
    TRIAL = "trial"
    PAUSED = "paused"
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    PAST_DUE = "past_due"
    
class VideoQuality(Enum):
    SD_480P = "480p"
    HD_720P = "720p"
    HD_1080P = "1080p"
    UHD_4K = "4K"
    UHD_8K = "8K"
    
class ExperimentVariant(Enum):
    CONTROL = "control"
    TREATMENT_A = "traetment_a"
    TREATMENT_B = "treatment_b"
    TREATMENT_C = "treatment_c"
    
@dataclass
class PlaybackEvent:
    Captures video platback events with telemetry data.
    Partition by: event_date, event_hour, user_id
    even_id: str = field(default_factory=lambda: str(vvid4()))
    event_type: EventType = EventType.PLAY_START
    event_timestamp: datetime = field(default_factory=datetime.utcnow)
    
    user_id: str = ""
    session_id: str = ""
    device_id: str = ""
    
    content_id = str = ""
    content_title: str = ""
    content_type: ContentType = ContentType.MOVIE
    
    position_seconds: int = 0