# 🤖 Aider AI Development Instructions

## 🎯 Mission: Complete Full-Stack Project Implementation

**Your task**: Build the entire "미용실 고객 관리 앱을 만들고 싶어. 예약과 고객 히스토리가 중요해." application from scratch using the specifications in PROJECT_CONTEXT.md.

## 📋 **STEP 1: Initialize Project Structure**

Create complete Next.js project with all necessary files:

```bash
# First, create the project foundation
/ask Create a complete Next.js 14 project structure with:
- package.json with all necessary dependencies
- next.config.js
- tsconfig.json  
- tailwind.config.ts
- postcss.config.js
- .eslintrc.json
- .gitignore
- .env.example

# Add all dependencies for: Next.js 14, Next.js API Routes + Server Actions, PostgreSQL + Prisma
```

## 📋 **STEP 2: Database Design**

```bash
/ask Create complete Prisma schema with:
- All models needed for the features listed in PROJECT_CONTEXT.md
- Proper relationships and indexes
- Multi-tenancy support if required
- Audit fields (createdAt, updatedAt)
```

## 📋 **STEP 3: Authentication & Core Setup**

```bash
/ask Implement NextAuth.js authentication with:
- Complete auth configuration
- User model integration
- Session management
- Protected route middleware
```

## 📋 **STEP 4: Feature Implementation**

Implement each feature in this exact order:


### Phase 1: 실시간 예약 시스템
```bash
/ask Implement "실시간 예약 시스템" feature:
- Description: 고객이 실시간으로 예약하고 즉시 확인할 수 있는 시스템
- Expert guidance: Dr. Riley Chen: Server Components로 실시간 업데이트가 부드러워요
- Create all necessary API routes/server actions
- Build complete UI components
- Add proper validation and error handling
- Ensure mobile responsiveness
```

### Phase 2: 고객 히스토리 관리
```bash
/ask Implement "고객 히스토리 관리" feature:
- Description: 고객별 방문 기록, 선호 스타일리스트, 알레르기 정보 관리
- Expert guidance: Dr. Casey Kim: 개인정보는 암호화해서 안전하게 저장할게요
- Create all necessary API routes/server actions
- Build complete UI components
- Add proper validation and error handling
- Ensure mobile responsiveness
```

### Phase 3: 직원 스케줄 관리
```bash
/ask Implement "직원 스케줄 관리" feature:
- Description: 직원별 근무 시간, 휴가, 고객 배정 관리
- Expert guidance: Dr. Samuel Lee: 직관적인 드래그앤드롭으로 쉽게 관리할 수 있어요
- Create all necessary API routes/server actions
- Build complete UI components
- Add proper validation and error handling
- Ensure mobile responsiveness
```

### Phase 4: 다중 매장 통합 관리
```bash
/ask Implement "다중 매장 통합 관리" feature:
- Description: 5개→50개 매장까지 확장 가능한 멀티테넌트 아키텍처
- Expert guidance: Dr. Casey Kim: Row Level Security로 매장별 데이터 완전 격리
- Create all necessary API routes/server actions
- Build complete UI components
- Add proper validation and error handling
- Ensure mobile responsiveness
```


## 📋 **STEP 5: UI/UX Implementation**

```bash
/ask Create complete UI based on warm-emotional theme:
- booking-centric layout structure
- Responsive navigation
- Professional styling with Tailwind CSS
- Loading states and error boundaries
- Accessibility compliance (WCAG 2.1)
```

## 📋 **STEP 6: Final Polish**

```bash
/ask Complete final optimization:
- Fix all TypeScript errors
- Optimize performance
- Add proper error handling
- Ensure all features work together
- Add production-ready configurations
```

## 🛠 **Technical Requirements**

### Architecture
- **Framework**: Next.js 14
- **Backend**: Next.js API Routes + Server Actions  
- **Database**: PostgreSQL + Prisma
- **Deployment**: Vercel + Vercel Postgres

### Code Quality Standards
- TypeScript for type safety
- Server Components where possible
- Server Actions for form handling
- Proper error boundaries
- Input validation with Zod
- Security best practices

### Performance Requirements
- Page load time: < 3 seconds
- Mobile-first responsive design
- Proper loading states
- Optimized database queries

## 🚨 **Critical Success Criteria**

1. ✅ **All selected features implemented and working**
2. ✅ **No TypeScript errors**
3. ✅ **Mobile responsive design**
4. ✅ **Proper authentication and security**
5. ✅ **Production-ready code quality**

## 💡 **Aider Pro Tips**

- Always run `/add PROJECT_CONTEXT.md` first
- Use `/ask` for complex implementations
- Test each feature before moving to the next
- Ask for clarification if requirements are unclear
- Focus on code quality and maintainability

**Remember**: You're building a complete, production-ready application. Don't leave anything half-implemented!

---

🎯 **Goal**: Deliver a fully functional application that exactly matches the specifications in PROJECT_CONTEXT.md
