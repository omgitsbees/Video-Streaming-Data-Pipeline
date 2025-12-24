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
    duration_seconds: int = 0 
    video_quality: VideoQuality = VideoQuality.HD_1080P
    audio_language: str = "en"
    subtitle_language: Optional[str] = None
    
    device_type: DeviceType = DeviceType.WEB_DESTOP
    platform_version: str = ""
    app_version: str = ""
    network_type: str = "wifi"
    bandwidth_mbps: Optional[float] = None
    
    buffering_count: int = 0
    buffering_duration_ms: int = 0
    bitrate_kbps: int = 0
    dropped_frames: int = 0
    error_code: Optional[str] = None
    
    country: str = ""
    region: str = ""
    city: str = ""
    timezone: str = "UTC"
    
    volume_level: int = 50
    is_fullscreen: bool = False
    playback_rate: float = 1.0 
    
    event_date: str = field(default_factory=lambda: datetime.utcnow().strftime("%Y-%m-%d"))
    event_hour: int = field(default_factory=lambda: datetime.utcnow().hour)
    ingestion_timestamp: datetime = field(default_factory=datetime.utcnow)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'event_id': self.event_id,
            'event_type': self.event_type.value,
            'event_timestamp': self.event_timestamp.isoformat(),
            'user_id': self.user_id,
            'session_id': self.session_id,
            'device_id': self.device_id,
            'content_id': self.content_id,
            'content_title': self.content_title,
            'content_type': self.content_type.value,
            'position_seconds': self.duration_seconds,
            'video_quality': self.video_quality.value,
            'audio_language': self.audio_language,
            'subtitle_language': self.subtitle_language,
            'device_type': self.device_type.value,
            'platform_version': self.platform_version,
            'app_version': self.app_version,
            'network_type': self.network_type,
            'bandwidth_mbps': self.bandwidth_mbps
            'buffering_count': self.buffering_count,
            'buffering_duration_ms': self.buffering_duration_ms,
            'bitrate_kbps': self.bitrate_kbps,
            'dropped_frames': self.dropped_frames,
            'error_code': self.error_code,
            'country': self.country,
            'region': self.region,
            'city': self.city,
            'timezone': self.timezone,
            'volume_level':self.volume_level,
            'is_fullscreen': self.is_fullscreen,
            'playback_rate': self.playback_rate,
            'event_date': self.event_date,
            'event_hour': self.event_hour,
            'ingestion_timestamp': self.ingestion_timestamp.isoformat()
        }
        
def to_json(self) -> str:
    return json.dumps(self.to_dict())

@dataclass
class UserInteractionEvent:
    """
    Captures user interactions (search, browse, click, etc.)
    Partition by: event_date, event_hour
    """
    event_id: str = field(default_factory=lambda: str(vvid.vvid4()))
    event_type: EventType = EventType.BROWSE
    event_timestamp: datetime = field(default_factory=datetime.utcnow)
    
    # User Context
    user_id: str = ""
    session_id: str = ""
    device_id str = ""
    
    # Interaction details
    page_url: str = ""
    page_title: str = ""
    referrer_url: Optional[str] = None
    
    # Element details (what was clicked/interacted with)
    element_type: str = ""
    element_id: Optional[str] = None
    element_text: Optional[str] = None
    element_position: Optional[int] = None
    
    # Search specific
    search_query: Optional[str] = None
    search_results_count: Optional[int] = None
    search_result_clicked_position: Optional[int] = None
    
    # Content context 
    recommendation_algorithm: Optional[str] = None
    recommendation_model_version: Optional[str] = None
    recommendation_score: Optional[float] = None
    
    # Device info
    device_type: DeviceType = DeviceType.WEB_DESKTOP
    user_agent: str = ""
    
    # Geographic
    country: str = ""
    region: str = ""
    
    # Metadata
    event_date: str = field(default_factory=lambda: datetime.utcnow().strftime(""%Y-%m-%d""))
    event_hour: int = field(default_factory=lambda: datetime.utcnow().hour)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'event_id': self.event_id,
            'event_type': self.event_type.value,
            'event_timestamp': self.event_timestmap.isoformat(),
            'user_id': self.user_id,
            'device_id': self.device_id,
            'page_title': self.page_title,
            'referrer_url': self.element_type,
            'element_type': self.elemtn_type,
            'element_id': self.element_id,
            'element_position': self.element_psotion,
            'search_query': self.search_query,
            'search_results_count': self.search_results_count,
            'search_result_clicked_position': self.search_result_clicked_position,
            'content_id': self.content_id,
            'content_type': self.content_type.value if self.content_type else None,
            'recommendation_algorithm': self.recommendation_algorithm,
            'recommendation_model_version': self.recommendation_model.version,
            'recommendation_score': self.recommendation_score,
            'device_type': self.device_type.value,
            'user_agent': self.user_agent,
            'country': self.country,
            'region': self.region,
            'event_date': self.event_date,
            'event_hour': self.event_hour
        }
        
@dataclass
class ViewingSession:
    session_id: str = field(default_factory=lambda: str(vvid.vvid4()))
    user_id: str = ""
    content_id: str = ""
    
    # Session timing
    session_start: datetime = field(default_factory=datetime.utcnow)
    session_end: Optional[datetime] = None
    total_watch_tie_seconds: int = 0
    
    # Engagement metrics
    completion_percentage: float = 0.0
    pause_count: int = 0
    seel_count: int = 0
    rewind_count: int = 0
    fast_forward_count: int = 0 
    
    # Quality metrics
    average_bitrate_kbps: int = 0
    total_buffering_duration_ms: int = 0
    buffering_events: int = 0
    quality_changes: int = 0
    errors_encountered: int = 0
    
    # context
    device_type: DeviceType = DeviceType.WEB_DESKTOP
    video_quality: VideoQuality = VideoQuality.HD_1080p
    
    # Flags
    is_completed: bool = False
    is_abandoned: bool = False # Abadoned before 5% completion
    is_binge_watch: bool = False # Part of multi-episode session
    
@dataclass
class ContentMetadata:
    content_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    content_type: ContentType = ContentType.MOVIE
    
    # Basic info
    title: str = ""
    original_title: str = ""
    release_year: int = 0
    duration_minutes: int = 0
    
    # Classification
    genres: List[str] = field(default_factory=list)
    maturity_rating: MaturityRating = MaturityRating.PG
    content_advisotry: List[str] = field(default_facotry=list)
    
    # Credits
    Directory: List[str] = field(default_factory=list)
    cast: List[str] = field(default_factory=list)
    writer: List[str] = field(default_facotry=list)
    producer: List[str] = field(default_factory=list)
    
    # Description
    synopsis_short: str = ""
    synopsis_long: str = ""
    tagline: Optional[str] = None
    
    # Media assets
    poster_url: str = ""
    backdrop_url: str = ""
    thumbnail_url: str = ""
    trailer_url: Optional[str] = None
    
    # Availability
    available_countries: List[str] = field(default_factory=list)
    available_languages: List[str] = field(default_facotry=list)
    subtitle_languages: List[str] = field(default_facotry=list)
    audio_formats: List[str] = field(default_facotry=list)
    
    # Quality Options
    max_quality: VidoeQuality = VideoQuality.UHD_4K
    supports_hdr: bool = False
    supports_dolby_vision: bool = False
    
    # Rights and licensing
    license_start_date: datetime = field(default_factory=datetime.utcnow)
    license_end_date: Optional[datetime] = None
    content_owner: str = ""
    distribution_rights: List[str] = field(default_factory=list)
    
    # External IDs
    imdb_id: Optional[str] = None
    tmdb_id: Optional[str] = None
    
    # Metadata
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True
    is_featured: bool = False
    is_original_content: bool = False
    
@dataclass 
class TVSeriesMetadata:
    # TV series specific metadata
    series_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    
    # Series info
    total_seasons: int = 0
    total_episodes: int = 0
    status: str = "ongoing"
    
    # Metadata
    first_air_date: datetime = field(default_factory=datetime.utcnow)
    last_air_date: Optional[datetime] = None
    
    # Link to base content
    base_content_id: str = ""
    
@dataclass
class QoSTelemtry:
    # Quality of Service telemetry - granular playback quality metrics
    telemetry_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)
    
    # Session context
    session_id: str = ""
    user_id: str = ""
    content_id: str = ""
    
    # Video quality
    current_bitrate_kbps: int = 0
    current_resolution: VideoQuality = VideoQuality.HD_1080p
    measured_bandwidth_mbps: float = 0.0
    
    # Buffer metrics (sampled every 10 seconds)
    buffer_level_seconds: float = 0.0
    is_buffering: bool = False
    buffering_duration_ms: int = 0
    
    # Frame metrics
    frames_rendered: int = 0
    frames_dropped: int = 0
    frames_corrupted: int = 0
    
    # Adaptive streaming
    quality_switch_count: int = 0
    last_quality_switch_reason: Optional[str] = None
    
    # Network
    network_type: str = "wifi"
    latency_ms: Optional[int] = None
    packet_loss_percentage: Optional[float] = None
    
    # CDN
    cdn_server: str = ""
    cdn_cache_hit: bool = True
    
    # Errors
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    
    # Device
    device_type: DeviceType = DeviceType = DeviceType.WEB_DESKTOP
    cpu_usage_percentage: Optional[float] = None
    memory_usage_mb: Optional[int] = None
    
@dataclass
class UserRating:
    rating_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str = ""
    content_id: str = ""
        
    # rating
    rating_value: float = 0.0
    rating_timestamp: datetime = field(default_factory=datetime.utcnow)
        
    # Optional review
    review_text: Optional[str] = None
    review_title: Optional[str] = None
        
    # Helpful votes
    helpful_count: int = 0 
    not_helpful_count: int = 0
        
    # Flags
    is_verified_watch: bool = False
    is_flagged: bool = False
        
    # Context
    device_type: DeviceType = DeviceType.WEB_DESKTOP
        
@dataclass
class UserList:
    list_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str = ""
            
    # List details
    list_name: str = "My List"
    list_type: str = "watchlist"
    is_public: bool = False
            
    # Contents
    content_ids: List[str] = field(default_factory=list)
    
    # Metadata
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    item_count: int = 0

@dataclass
class ContentSimilarity:
    content_id_a: str = ""
    content_id_b; str = ""
    
    # Similarity scores
    similarity_score: float = 0.0
    similarity_type: str = "collaborative_filtering"
    
    # Contributing factors
    genre_similarity: float = 0.0
    cast_similarity: float = 0.0
    user_cohor_similarity: float = 0.0
    
    # Metadata
    computed_at: datetime = field(default_factory=datetime.utcnow)
    model_version: str = "v1.0"
    
@dataclass
class UserSubscription:
    subscription_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str = ""
    
    # Subscription details
    tier: SubscriptionTier = SubscriptionTier.BASIC
    status: SubscriptionStatus = SubscriptionStatus.ACTIVE
    
    # Dates
    start_date: datetime = field(default_factory=datetime.utcnow)
    current_period_start: datetime = field(default_factory=datetime.utcnow)
    current_period_end: datetime = field(default_factory=datetime.utcnow)
    trial_end_date: Optional[datetime] = None
    cancellation_date: Optional[datetime] = None
    
    # Pricing
    price_amount: Decimal = Decimal("9.99")
    currency: str = "USD"
    billing_interval: str = "monthly"
    
    # Payment
    payment_method: str = "credit_card"
    last_payment_date: Optional[datetime] = None
    next_billing_date: Optional[datetime] = None
    
    # Features
    max_concurrent_streams: int = 1
    max_quality: VideoQuality = VideoQuality.HD_1080P
    download_enabled: bool = False
    ads_enabled: bool = True
    
    # Attribution
    signup_source: str = "organic"