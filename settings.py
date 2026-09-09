import os, json

class Settings:
    
    instance = None
    
    @staticmethod
    def get_instance() -> "Settings":
        if Settings.instance is None: Settings.instance = Settings()
        
        return Settings.instance
    
    telegram_token = ""
    telegram_chat_id = ""
    
    cirlce_upload = False

    max_time_seconds = 3600
    minimum_likes = 500
    minimum_replies = 5
    disable_comments = False
    max_posts_on_post = 5
    min_views_on_post = 500
    
    avatar_folder = ""

    set_image_on_rec = True
    set_image_on_warm = True
    
    posts_file = ""
    accounts_file = ""
    proxies_file = ""
    text_file = ""
    search_query_file = ""
    images = []
    spam_method = 0
    account_format = 0
    threads = 1
    comments = 20
    captcha_key = ""
    asocks_key = ""
    unique_photo = 0
    
    country_code = ""
    state = ""
    city = ""
    asn = 0
    
    apply_bg = False
    snow = False
    ai_generation = False
    noise_enabled = False
    draw_lines = False
    random_position = False
    generate_background = False
    emoji = False
    mirror_x = False
    mirror_y = False
    color_correction = False
    random_size = False
    noise_all = False
    
    snow_count = 100
    snow_size_min = 1
    snow_size_max = 5
    emoji_opacity = 1
    background_scale = 1
    image_opacity = 1
    emoji_count = 30
    emoji_scale_factor = 1.2
    noise_intensity = 0.1
    line_thickness = 1
    line_width = 5
    rotate_angle_min = 0
    rotate_angle_max = 0
    
    quality = 100
    final_image_size = 100
    
    bg_images_folder = ""
    snow_dir = ""
    shape = "portrait"
    prompt = ""
    negative_prompt = ""
    
    def __init__(self, data: str | None = None):
        if data is not None:
            self.from_json(data)
        else:
            if os.path.exists("C:/Threads/settings.json"):
                with open("C:/Threads/settings.json", "r", encoding="utf-8") as f:
                    self.from_json(f.read())
    
    def __str__(self):
        return json.dumps({
            "telegram_token": self.telegram_token,
            "telegram_chat_id": self.telegram_chat_id,

            "cirlce_upload": self.cirlce_upload,

            "set_image_on_rec": self.set_image_on_rec,
            "set_image_on_warm": self.set_image_on_warm,

            "max_time_seconds": self.max_time_seconds,
            "minimum_likes": self.minimum_likes,
            "minimum_replies": self.minimum_replies,
            "disable_comments": self.disable_comments,
            "max_posts_on_post": self.max_posts_on_post,
            "min_views_on_post": self.min_views_on_post,

            "avatar_folder": self.avatar_folder,
            
            "posts_file": self.posts_file,
            "accounts_file": self.accounts_file,
            "proxies_file": self.proxies_file,
            "text_file": self.text_file,
            "search_query_file": self.search_query_file,
            "spam_method": self.spam_method,
            "account_format": self.account_format,
            "images": self.images,
            "threads": self.threads,
            "comments": self.comments,
            "captcha_key": self.captcha_key,
            "asocks_key": self.asocks_key,
            "unique_photo": self.unique_photo,
            
            "country_code": self.country_code,
            "state": self.state,
            "city": self.city,
            "asn": self.asn,
            
            "apply_bg": self.apply_bg,
            "snow": self.snow,
            "ai_generation": self.ai_generation,
            "noise_enabled": self.noise_enabled,
            "draw_lines": self.draw_lines,
            "random_position": self.random_position,
            "generate_background": self.generate_background,
            "emoji": self.emoji,
            "mirror_x": self.mirror_x,
            "mirror_y": self.mirror_y,
            "color_correction": self.color_correction,
            "random_size": self.random_size,
            "noise_all": self.noise_all,
            "snow_count": self.snow_count,
            "snow_size_min": self.snow_size_min,
            "snow_size_max": self.snow_size_max,
            "emoji_opacity": self.emoji_opacity,
            "background_scale": self.background_scale,
            "image_opacity": self.image_opacity,
            "emoji_count": self.emoji_count,
            "emoji_scale_factor": self.emoji_scale_factor,
            "noise_intensity": self.noise_intensity,
            "line_thickness": self.line_thickness,
            "line_width": self.line_width,
            "rotate_angle_min": self.rotate_angle_min,
            "rotate_angle_max": self.rotate_angle_max,
            "quality": self.quality,
            "final_image_size": self.final_image_size,
            "bg_images_folder": self.bg_images_folder,
            "snow_dir": self.snow_dir,
            "shape": self.shape,
            "prompt": self.prompt,
            "negative_prompt": self.negative_prompt,
        })
        
    def save(self):
        with open("C:/Threads/settings.json", "w", encoding="utf-8") as f:
            f.write(str(self))
            
    def edit(self, name, value):
        setattr(self, name, value)
        self.save()
    
    def from_json(self, str):
        js = json.loads(str)
        
        self.telegram_token = js.get("telegram_token", "")
        self.telegram_chat_id = js.get("telegram_chat_id", "")

        self.cirlce_upload = js.get("cirlce_upload", False)

        self.set_image_on_rec = js.get("set_image_on_rec", self.set_image_on_rec)
        self.set_image_on_warm = js.get("set_image_on_warm", self.set_image_on_warm)

        self.max_time_seconds = js.get("max_time_seconds", self.max_time_seconds)
        self.minimum_likes = js.get("minimum_likes", self.minimum_likes)
        self.minimum_replies = js.get("minimum_replies", self.minimum_replies)
        self.disable_comments = js.get("disable_comments", self.disable_comments)
        self.max_posts_on_post = js.get("max_posts_on_post", self.max_posts_on_post)
        self.min_views_on_post = js.get("min_views_on_post", self.min_views_on_post)

        self.avatar_folder = js.get("avatar_folder", self.avatar_folder)
        
        self.posts_file = js.get("posts_file", "")
        self.accounts_file = js.get("accounts_file", "")
        self.proxies_file = js.get("proxies_file", "")
        self.text_file = js.get("text_file", "")
        self.search_query_file = js.get("search_query_file", "")
        self.images = js.get("images", [])
        self.spam_method = js.get("spam_method", 0)
        self.account_format = js.get("account_format", 0)
        self.threads = js.get("threads", 1)
        self.comments = js.get("comments", 20)
        self.captcha_key = js.get("captcha_key", "")
        self.asocks_key = js.get("asocks_key", "")
        self.unique_photo = js.get("unique_photo", 0)
        
        self.country_code = js.get("country_code", "")
        self.state = js.get("state", "")
        self.city = js.get("city", "")
        self.asn = js.get("asn", 0)
        
        self.apply_bg = js.get("apply_bg", self.apply_bg)
        self.snow = js.get("snow", self.snow)
        self.ai_generation = js.get("ai_generation", self.ai_generation)
        self.noise_enabled = js.get("noise_enabled", self.noise_enabled)
        self.draw_lines = js.get("draw_lines", self.draw_lines)
        self.random_position = js.get("random_position", self.random_position)
        self.generate_background = js.get("generate_background", self.generate_background)
        self.emoji = js.get("emoji", self.emoji)
        self.mirror_x = js.get("mirror_x", self.mirror_x)
        self.mirror_y = js.get("mirror_y", self.mirror_y)
        self.color_correction = js.get("color_correction", self.color_correction)
        self.random_size = js.get("random_size", self.random_size)
        self.noise_all = js.get("noise_all", self.noise_all)
        self.snow_count = js.get("snow_count", self.snow_count)
        self.snow_size_min = js.get("snow_size_min", self.snow_size_min)
        self.snow_size_max = js.get("snow_size_max", self.snow_size_max)
        self.emoji_opacity = js.get("emoji_opacity", self.emoji_opacity)
        self.background_scale = js.get("background_scale", self.background_scale)
        self.image_opacity = js.get("image_opacity", self.image_opacity)
        self.emoji_count = js.get("emoji_count", self.emoji_count)
        self.emoji_scale_factor = js.get("emoji_scale_factor", self.emoji_scale_factor)
        self.noise_intensity = js.get("noise_intensity", self.noise_intensity)
        self.line_thickness = js.get("line_thickness", self.line_thickness)
        self.line_width = js.get("line_width", self.line_width)
        self.rotate_angle_min = js.get("rotate_angle_min", self.rotate_angle_min)
        self.rotate_angle_max = js.get("rotate_angle_max", self.rotate_angle_max)
        self.quality = js.get("quality", self.quality)
        self.final_image_size = js.get("final_image_size", self.final_image_size)
        self.bg_images_folder = js.get("bg_images_folder", self.bg_images_folder)
        self.snow_dir = js.get("snow_dir", self.snow_dir)
        self.shape = js.get("shape", self.shape)
        self.prompt = js.get("prompt", self.prompt)
        self.negative_prompt = js.get("negative_prompt", self.negative_prompt)