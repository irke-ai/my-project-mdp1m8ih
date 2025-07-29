# Project Context

## Original Request
미용실 고객 관리 앱을 만들고 싶어. 예약과 고객 히스토리가 중요해.

## Expert Consultation Summary

This project was designed through consultation with 4 AI experts.

## Expert Insights

This project was designed through consultation with 4 AI experts:
- Dr. Riley Chen (System Architecture)
- Dr. Casey Kim (Database Design)  
- Dr. Samuel Lee (UI/UX)
- Dr. Maria Gonzalez (DevOps & Infrastructure)


## Technical Requirements

### Frontend Requirements
- Framework: Next.js 14
- Styling: Tailwind CSS
- State Management: As needed (Context API, Zustand, etc.)
- Form Handling: React Hook Form with Zod validation

### Backend Requirements
- API: Next.js API Routes + Server Actions
- Authentication: NextAuth.js
- Database ORM: Prisma
- Validation: Zod schemas

### Database Requirements
- Database: PostgreSQL + Prisma
- Multi-tenancy: Not required
- Audit trails: Required for all major entities

### Infrastructure Requirements
- Deployment: Vercel + Vercel Postgres
- CI/CD: GitHub Actions
- Monitoring: Vercel Analytics (if using Vercel)

## Design Requirements

### Theme: warm-emotional
- Primary colors: Professional blues and grays
- Typography: Clean, modern sans-serif
- Spacing: Consistent, breathable layout

### Layout: booking-centric
- Navigation: Top navigation
- Mobile: Fully responsive, mobile-first approach
- Accessibility: WCAG 2.1 AA compliance

## Feature Details


### 실시간 예약 시스템
**Description**: 고객이 실시간으로 예약하고 즉시 확인할 수 있는 시스템
**Priority**: Low
**Technical Requirements**:
- Dr. Riley Chen: Server Components로 실시간 업데이트가 부드러워요



### 고객 히스토리 관리
**Description**: 고객별 방문 기록, 선호 스타일리스트, 알레르기 정보 관리
**Priority**: Low
**Technical Requirements**:
- Dr. Casey Kim: 개인정보는 암호화해서 안전하게 저장할게요



### 직원 스케줄 관리
**Description**: 직원별 근무 시간, 휴가, 고객 배정 관리
**Priority**: Low
**Technical Requirements**:
- Dr. Samuel Lee: 직관적인 드래그앤드롭으로 쉽게 관리할 수 있어요
- Dependencies: realtime_booking


### 다중 매장 통합 관리
**Description**: 5개→50개 매장까지 확장 가능한 멀티테넌트 아키텍처
**Priority**: Low
**Technical Requirements**:
- Dr. Casey Kim: Row Level Security로 매장별 데이터 완전 격리
- Dependencies: realtime_booking, staff_scheduling


## Performance Requirements
- Page load time: < 3 seconds
- Time to Interactive: < 5 seconds
- Lighthouse score: > 90

## Security Requirements
- Authentication: Required for all protected routes
- Authorization: Role-based access control
- Data encryption: HTTPS only
- Input validation: All user inputs must be validated

## Scalability Considerations
- Expected users: 100+ concurrent users
- Database optimization: Proper indexing and query optimization
- Caching strategy: Implement where appropriate

## Development Phases


### Phase 1: Phase 1: 기초 설계 및 환경 구축 (2주)
Deliverables:
- 데이터베이스 스키마 완성
- Next.js 프로젝트 구조 설계
- CI/CD 파이프라인 구축


### Phase 2: Phase 2: 핵심 기능 개발 (4-5주)
Deliverables:
- 실시간 예약 시스템
- 고객 히스토리 관리
- 직원 스케줄 관리


### Phase 3: Phase 3: 고급 기능 구현 (3-4주)
Deliverables:
- 다중 매장 통합 관리


### Phase 4: Phase 4: 테스트 및 배포 (2주)
Deliverables:
- 사용성 테스트
- 성능 최적화
- 운영 환경 배포
- 문서화 완료


## Success Criteria
1. All selected features implemented and working
2. Performance benchmarks met
3. Security best practices followed
4. Code is maintainable and well-documented
5. Application is production-ready

---

This context should guide all development decisions. When in doubt, prioritize user experience, security, and maintainability.
