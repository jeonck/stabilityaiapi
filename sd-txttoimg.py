import requests
import json
import time

# Stable Diffusion API 엔드포인트
url = "https://stablediffusionapi.com/api/v1/enterprise/text2img"

# API 키 (사용자의 API 키로 대체해야 함)
api_key = "ㅇㅇㅇ"

# 텍스트 입력
prompt_text = "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K"

# 부정 프롬프트
negative_prompt_text = "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime"

# 요청에 필요한 데이터
payload = json.dumps({
  "key": api_key,
  "model_id": "aingdiffusion-v14-1",
  "prompt": prompt_text,
  "negative_prompt": negative_prompt_text,
  "width": "512",
  "height": "512",
  "samples": "1",
  "num_inference_steps": "30",
  "safety_checker": "no",
  "enhance_prompt": "yes",
  "seed": None,
  "guidance_scale": 7.5,
  "multi_lingual": "no",
  "panorama": "no",
  "self_attention": "no",
  "upscale": "no",
  "embeddings_model": None,
  "tomesd": "yes",
  "use_karras_sigmas": "yes",
  "vae": None,
  "lora_strength": None,
  "lora_model": None,
  "scheduler": "UniPCMultistepScheduler",
  "webhook": None,
  "track_id": None
})

# 요청 헤더
headers = {
  'Content-Type': 'application/json'
}

# 수행 시간 측정 시작
start_time = time.time()

# POST 요청 보내기
response = requests.request("POST", url, headers=headers, data=payload)

# 수행 시간 측정 종료
end_time = time.time()
execution_time = end_time - start_time

# 응답 처리
try:
    result = response.json()
    # print(result)  # 디버깅을 위해 전체 응답 출력

    if result.get("status") == "success":
        image_url = result["output"][0]
        print(f"Generated Image URL: {image_url}")
    else:
        print(f"Error: {result.get('message')}")
except json.JSONDecodeError:
    print("Failed to parse response as JSON")
    print(response.text)
except (KeyError, TypeError) as e:
    print(f"Error processing response: {e}")
    print(result)
else:
    print(f"HTTP Error: {response.status_code}")

print(f"Execution time: {execution_time:.1f} seconds")