# AI 驱动设计工作流系统架构

## 1. 系统总览架构图

```mermaid
graph TB
    subgraph "知识层 Knowledge Layer"
        DL[知识分发总监<br/>Data Librarian<br/>TRACE框架]
        KB[(知识库<br/>Design Assets<br/>Trends & Cases)]
    end
    
    subgraph "智能体层 Agent Layer"
        A1[方案资讯官<br/>The Analyst<br/>BROKE框架]
        A2[彩平绘制师<br/>The Draftsman<br/>COSTAR框架]
        A3[三维建模师<br/>The Architect<br/>RTGO框架]
        A4[视觉艺术家<br/>The Stylist<br/>CARE框架]
        A5[杂志摄影师<br/>The Photographer<br/>RTF框架]
        A6[软装排版师<br/>The Curator<br/>ROSES框架]
    end
    
    subgraph "输入层 Input Layer"
        I1[项目需求]
        I2[CAD线框图]
        I3[参考案例]
    end
    
    subgraph "输出层 Output Layer"
        O1[策略报告]
        O2[彩色平面图]
        O3[3D透视图]
        O4[风格效果图]
        O5[摄影级渲染]
        O6[方案排版]
    end
    
    I1 --> A1
    I2 --> A2
    I3 --> DL
    
    DL --> KB
    KB -.知识分发.-> A1
    KB -.知识分发.-> A2
    KB -.知识分发.-> A3
    KB -.知识分发.-> A4
    KB -.知识分发.-> A5
    KB -.知识分发.-> A6
    
    A1 --> O1
    A1 --> A2
    A2 --> O2
    A2 --> A3
    A3 --> O3
    A3 --> A4
    A4 --> O4
    A4 --> A5
    A5 --> O5
    A5 --> A6
    A6 --> O6
    
    style DL fill:#FFD700,stroke:#FF8C00,stroke-width:3px
    style A1 fill:#E8F4F8,stroke:#4A90E2
    style A2 fill:#FFF4E6,stroke:#F5A623
    style A3 fill:#F0E6FF,stroke:#9013FE
    style A4 fill:#FFE6F0,stroke:#E91E63
    style A5 fill:#E6F7FF,stroke:#00BCD4
    style A6 fill:#F0FFF0,stroke:#4CAF50
```

## 2. 工作流时序图

```mermaid
sequenceDiagram
    participant User as 用户
    participant DL as 知识分发总监
    participant A1 as 方案资讯官
    participant A2 as 彩平绘制师
    participant A3 as 三维建模师
    participant A4 as 视觉艺术家
    participant A5 as 杂志摄影师
    participant A6 as 软装排版师
    
    User->>DL: 上传设计趋势资料
    DL->>DL: TRACE解析<br/>(Task-Request-Action-Context-Example)
    DL->>A1: 分发策略知识卡片
    DL->>A4: 分发材质库更新
    
    User->>A1: 输入项目需求
    A1->>A1: BROKE分析<br/>(背景-角色-目标-关键结果-演变)
    A1->>User: 输出策略报告
    
    User->>A2: 上传CAD线框图
    A2->>A2: COSTAR处理<br/>(上下文-目标-风格-语气-受众-回复)
    A2->>User: 输出彩色平面图
    
    A2->>A3: 传递2D布局
    A3->>A3: RTGO建模<br/>(角色-任务-目标-操作)
    A3->>User: 输出3D透视图
    
    A3->>A4: 传递3D模型
    A4->>A4: CARE渲染<br/>(上下文-行动-结果-示例)
    A4->>User: 输出风格效果图
    
    A4->>A5: 传递渲染结果
    A5->>A5: RTF摄影<br/>(角色-任务-格式)
    A5->>User: 输出摄影级渲染
    
    A5->>A6: 传递最终图像
    A6->>A6: ROSES排版<br/>(角色-目标-场景-方案-步骤)
    A6->>User: 输出完整方案
```

## 3. 提示词框架映射矩阵

```mermaid
graph LR
    subgraph "阶段 0: 前期策划"
        F1[BROKE框架]
        F1 --> F1A[Background 背景]
        F1 --> F1B[Role 角色]
        F1 --> F1C[Objectives 目标]
        F1 --> F1D[Key Results 关键结果]
        F1 --> F1E[Evolve 演变]
    end
    
    subgraph "阶段 1: 平面表达"
        F2[COSTAR框架]
        F2 --> F2A[Context 上下文]
        F2 --> F2B[Objective 目标]
        F2 --> F2C[Style 风格]
        F2 --> F2D[Tone 语气]
        F2 --> F2E[Audience 受众]
        F2 --> F2F[Response 回复]
    end
    
    subgraph "阶段 2: 空间转换"
        F3[RTGO框架]
        F3 --> F3A[Role 角色]
        F3 --> F3B[Task 任务]
        F3 --> F3C[Goal 目标]
        F3 --> F3D[Operation 操作]
    end
    
    subgraph "阶段 3: 风格迭代"
        F4[CARE框架]
        F4 --> F4A[Context 上下文]
        F4 --> F4B[Action 行动]
        F4 --> F4C[Result 结果]
        F4 --> F4D[Example 示例]
    end
    
    subgraph "阶段 4: 摄影表达"
        F5[RTF框架]
        F5 --> F5A[Role 角色]
        F5 --> F5B[Task 任务]
        F5 --> F5C[Format 格式]
    end
    
    subgraph "阶段 5: 后期输出"
        F6[ROSES框架]
        F6 --> F6A[Role 角色]
        F6 --> F6B[Objective 目标]
        F6 --> F6C[Scenario 场景]
        F6 --> F6D[Expected Solution 方案]
        F6 --> F6E[Steps 步骤]
    end
    
    style F1 fill:#E8F4F8
    style F2 fill:#FFF4E6
    style F3 fill:#F0E6FF
    style F4 fill:#FFE6F0
    style F5 fill:#E6F7FF
    style F6 fill:#F0FFF0
```

## 4. 知识分发机制 (TRACE)

```mermaid
graph TD
    subgraph "知识输入"
        IN1[大师作品集]
        IN2[行业报告]
        IN3[设计趋势]
        IN4[材质库]
    end
    
    subgraph "TRACE解析引擎"
        T[Task<br/>提取核心设计语言]
        R[Request<br/>转化为量化参数]
        A[Action<br/>封装为知识卡片]
        C[Context<br/>关联机器人环境]
        E[Example<br/>生成参考样张]
        
        T --> R --> A --> C --> E
    end
    
    subgraph "知识卡片库"
        KC1[审美参数卡片<br/>f/2.8景深效果]
        KC2[材质参数卡片<br/>微水泥反射率]
        KC3[趋势策略卡片<br/>2025米兰展]
        KC4[摄影参数卡片<br/>焦段-构图]
    end
    
    subgraph "智能体订阅"
        S1[方案资讯官<br/>订阅趋势策略]
        S2[视觉艺术家<br/>订阅材质库]
        S3[杂志摄影师<br/>订阅摄影参数]
    end
    
    IN1 --> T
    IN2 --> T
    IN3 --> T
    IN4 --> T
    
    E --> KC1
    E --> KC2
    E --> KC3
    E --> KC4
    
    KC1 -.实时同步.-> S2
    KC2 -.实时同步.-> S2
    KC3 -.实时同步.-> S1
    KC4 -.实时同步.-> S3
    
    style T fill:#FFE6E6
    style R fill:#FFF4E6
    style A fill:#E6F7FF
    style C fill:#F0E6FF
    style E fill:#E6FFE6
```

## 5. 摄影美学控制系统

```mermaid
graph TB
    subgraph "摄影参数控制"
        P1[焦段控制]
        P2[光圈控制]
        P3[构图算法]
        P4[移轴逻辑]
    end
    
    subgraph "焦段映射"
        F1[16-24mm<br/>建筑张力<br/>广角透视]
        F2[50mm<br/>人眼观察<br/>自然视角]
        F3[85mm<br/>软装肌理<br/>细节特写]
    end
    
    subgraph "构图规则"
        C1[三分法则]
        C2[黄金分割]
        C3[对称构图]
        C4[引导线]
    end
    
    subgraph "移轴修正"
        TS1[垂直线条平行]
        TS2[透视畸变修正]
        TS3[专业建筑摄影]
    end
    
    subgraph "输出效果"
        OUT1[杂志级视觉]
        OUT2[叙事化表达]
        OUT3[专业摄影质感]
    end
    
    P1 --> F1
    P1 --> F2
    P1 --> F3
    
    P3 --> C1
    P3 --> C2
    P3 --> C3
    P3 --> C4
    
    P4 --> TS1
    P4 --> TS2
    P4 --> TS3
    
    F1 --> OUT1
    F2 --> OUT2
    F3 --> OUT3
    C1 --> OUT1
    TS1 --> OUT3
    
    style P1 fill:#E6F7FF
    style P2 fill:#FFF4E6
    style P3 fill:#F0E6FF
    style P4 fill:#FFE6F0
```

## 6. 六大智能体详细架构

```mermaid
mindmap
  root((AI设计团队))
    方案资讯官
      BROKE框架
        背景分析
        角色定义
        目标设定
        关键结果
        演变路径
      输出
        空间属性定义
        人群画像
        行业趋势
        逻辑底座
    彩平绘制师
      COSTAR框架
        上下文理解
        目标明确
        风格定义
        语气控制
        受众分析
        回复格式
      输出
        材质感表达
        阴影渲染
        动线引导
        彩色平面图
    三维建模师
      RTGO框架
        角色设定
        任务分解
        目标确认
        操作要求
      技术
        ControlNet
        2D转3D
        透视推演
      输出
        空间体量
        3D透视图
    视觉艺术家
      CARE框架
        上下文分析
        行动计划
        结果预期
        示例参考
      能力
        材质迁移
        灯光切换
        风格控制
      输出
        艺术化效果图
        一致性风格
    杂志摄影师
      RTF框架
        角色定位
        任务明确
        格式规范
      参数
        焦段16-85mm
        光圈f/1.4-f/16
        构图规则
      输出
        叙事化视觉
        摄影级渲染
    软装排版师
      ROSES框架
        角色明确
        目标设定
        场景分析
        方案设计
        步骤规划
      功能
        单品提取
        物料清单
        视觉排版
      输出
        完整方案
        专业排版
```

## 7. 系统数据流图

```mermaid
flowchart LR
    subgraph "输入数据"
        D1[项目需求文档]
        D2[CAD线框图]
        D3[参考图片]
        D4[设计趋势资料]
    end
    
    subgraph "处理流程"
        P1[需求分析<br/>BROKE]
        P2[平面绘制<br/>COSTAR]
        P3[3D建模<br/>RTGO]
        P4[风格渲染<br/>CARE]
        P5[摄影优化<br/>RTF]
        P6[方案排版<br/>ROSES]
    end
    
    subgraph "中间产物"
        M1[策略报告]
        M2[彩色平面图]
        M3[3D透视图]
        M4[风格效果图]
        M5[摄影级渲染]
    end
    
    subgraph "最终交付"
        F1[完整设计方案]
        F2[物料清单]
        F3[视觉排版]
    end
    
    D1 --> P1
    D2 --> P2
    D3 --> P1
    D4 --> P1
    
    P1 --> M1
    M1 --> P2
    P2 --> M2
    M2 --> P3
    P3 --> M3
    M3 --> P4
    P4 --> M4
    M4 --> P5
    P5 --> M5
    M5 --> P6
    
    P6 --> F1
    P6 --> F2
    P6 --> F3
    
    style P1 fill:#E8F4F8
    style P2 fill:#FFF4E6
    style P3 fill:#F0E6FF
    style P4 fill:#FFE6F0
    style P5 fill:#E6F7FF
    style P6 fill:#F0FFF0
```

---

## 图表说明

### 1. 系统总览架构图
展示了整个系统的三层架构:知识层、智能体层、输入输出层,以及它们之间的数据流动关系。

### 2. 工作流时序图
详细描述了从用户输入到最终交付的完整时序流程,包括各智能体之间的协作关系。

### 3. 提示词框架映射矩阵
将21种提示词框架中的6种核心框架映射到对应的设计阶段,展示每个框架的具体组成要素。

### 4. 知识分发机制
展示TRACE框架如何将外部知识转化为可执行的参数卡片,并分发给相应的智能体。

### 5. 摄影美学控制系统
详细说明摄影参数(焦段、光圈、构图、移轴)如何控制最终的视觉输出质量。

### 6. 六大智能体详细架构
使用思维导图形式展示每个智能体的框架、能力和输出。

### 7. 系统数据流图
从数据角度展示整个系统的输入、处理、中间产物和最终交付的流转过程。

---

**使用说明**: 这些 Mermaid 图表可以直接在支持 Mermaid 的 Markdown 编辑器中渲染,如 Obsidian、Typora、GitHub 等。
