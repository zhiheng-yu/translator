#!/bin/bash

# API 基础 URL
BASE_URL="http://localhost:6003"

echo -e "=== AI Translate API 测试脚本 ===\n"

# 1. 测试根路径
echo -e "[1] 测试根路径 GET /"
curl -X GET "${BASE_URL}/"
echo -e "\n"

# 2. 测试健康检查
echo -e "[2] 测试健康检查 GET /health"
curl -X GET "${BASE_URL}/health"
echo -e "\n"

# 3. 测试获取模型信息
echo -e "[3] 测试获取模型信息 GET /api/models"
curl -X GET "${BASE_URL}/api/models"
echo -e "\n"

# 4. 测试翻译接口 - 中文翻译为英文
echo -e "[4] 测试翻译接口 - 中文翻译为英文"
curl -X POST "${BASE_URL}/api/translate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "你好，世界！这是一个测试翻译。",
    "dst_lang": "English"
  }' \
  -s | jq '.'
echo -e ""

# 5. 测试翻译接口 - 英文翻译为中文
echo -e "[5] 测试翻译接口 - 英文翻译为中文"
curl -X POST "${BASE_URL}/api/translate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello, world! This is a test translation.",
    "dst_lang": "中文"
  }' \
  -s | jq '.'
echo -e ""

# 6. 测试翻译接口 - 空内容（应该返回错误）
echo -e "[6] 测试翻译接口 - 空内容（预期错误）"
curl -X POST "${BASE_URL}/api/translate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "",
    "dst_lang": "English"
  }' \
  -s | jq '.'
echo -e ""

# 7. 测试翻译接口 - 长文本翻译
echo -e "[7] 测试翻译接口 - 长文本翻译"
curl -X POST "${BASE_URL}/api/translate" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "人工智能（Artificial Intelligence），简称AI，是计算机科学的一个分支，它企图了解智能的实质，并生产出一种新的能以人类智能相似的方式做出反应的智能机器。该领域的研究包括机器人、语言识别、图像识别、自然语言处理和专家系统等。",
    "dst_lang": "English"
  }' \
  -s | jq '.'
echo -e ""

echo -e "=== 测试完成 ==="
