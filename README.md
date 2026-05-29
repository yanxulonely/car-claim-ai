# 🚗 Car Claim AI

基于 AI 的车险定损智能助手。

## 🎯 功能

### 核心功能
- **智能定损** — 图片识别 + AI 分析，自动评估车辆损失
- **智能报价** — 基于定损结果，自动生成维修报价
- **案例管理** — 历史案例数据库，支持检索和学习
- **报告生成** — 自动生成定损报告，支持导出 PDF

### 辅助功能
- **知识库** — 车险定损专业知识库
- **法规查询** — 相关法规政策查询
- **风险评估** — 欺诈风险评估

## 📦 项目结构

```
car-claim-ai/
├── src/
│   ├── api/           # API 接口
│   ├── core/          # 核心业务逻辑
│   ├── models/        # AI 模型
│   └── utils/         # 工具函数
├── data/
│   ├── knowledge/     # 知识库
│   └── cases/         # 案例数据
├── docs/              # 文档
└── tests/             # 测试
```

## 🛠️ 技术栈

- **后端**: Python / FastAPI
- **AI**: MiMo / OpenAI / Claude
- **数据库**: PostgreSQL / Redis
- **前端**: Vue3 (可选)

## 📝 使用

```bash
# 克隆仓库
git clone https://github.com/yanxulonely/car-claim-ai.git

# 进入目录
cd car-claim-ai

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 填入 API Key

# 启动服务
python -m uvicorn main:app --reload
```

## 📄 License

MIT
