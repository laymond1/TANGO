<template>
  <div class="d-flex flex-column" style="gap: 15px; margin-left: -16px">
    <div>
      <div style="width: 100%" class="d-flex justify-center">
        <div style="gap: 15px" class="d-flex align-center">
          <v-btn class="mb-3" color="#4a80ff" width="380" dark @click="menualCreate">
            Manually Generation of Neural Networks
          </v-btn>

          <v-btn class="mb-3" color="#4a80ff" width="380" dark @click="autoCreate">
            Automatic Generation of Neural Networks
          </v-btn>
        </div>
      </div>
      <h4 class="ml-3 mb-3">
        Progress - {{ showContainerName(projectInfo?.container) }} {{ projectInfo?.container_status }}
      </h4>
      <v-card color="#DFDFDF" class="" style="border-radius: 4px" height="180">
        <div>
          <ProgressCanvas :running="projectInfo?.container" :status="projectInfo?.container_status" @start="start" />
        </div>
      </v-card>
    </div>
    <div>
      <h4 class="ml-3 mb-3">Log</h4>
      <v-card color="#000" class="ml-3" style="border-radius: 4px" height="200">
        <v-textarea
          ref="logs"
          id="log"
          dark
          filled
          no-resize
          :value="vale"
          height="200"
          style="font-size: 12px"
          readonly
          autofocus
        ></v-textarea>
      </v-card>
    </div>
  </div>
</template>
<script>
import { mapMutations, mapState } from "vuex";
import { ProjectNamespace, ProjectMutations } from "@/store/modules/project";

import ProgressCanvas from "@/modules/project/components/ProgressCanvas.vue";

import { ProjectType } from "@/shared/consts";

import { containerStart /* startContainer , stopContainer, getStatusResult*/, updateProjectType } from "@/api";
export default {
  components: { ProgressCanvas },
  props: {
    projectInfo: {
      default: () => ({})
    }
  },
  data() {
    return {
      vale: ``,
      running: ""
    };
  },

  computed: {
    ...mapState(ProjectNamespace, ["project"])
  },

  mounted() {
    this.$nextTick(() => {
      const element = document.getElementById("log");
      element.scrollTop = element.scrollHeight;
    });

    this.$EventBus.$on("logUpdate", this.updateLog);
  },

  methods: {
    ...mapMutations(ProjectNamespace, {
      SET_PROJECT: ProjectMutations.SET_PROJECT
    }),

    updateLog(log) {
      if (log.message !== "\n") {
        this.vale += log.message;
      }
      this.$nextTick(() => {
        const element = document.getElementById("log");
        element.scrollTop = element.scrollHeight;
      });
    },

    start(container) {
      console.log("projectInfo", this.projectInfo);

      this.$swal
        .fire({
          title: `${container}를 실행하시겠습니까?`,
          text: "",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "확인",
          cancelButtonText: "취소"
        })
        .then(async result => {
          if (result.isConfirmed) {
            this.$emit("restart", container);
            await updateProjectType(this.projectInfo.id, ProjectType.MANUAL);
            const res = await containerStart(container, this.projectInfo.create_user, this.projectInfo.id);
            this.vale += res.message;

            this.SET_PROJECT({
              project_type: ProjectType.MANUAL
            });
          }
        });

      this.SET_PROJECT({
        container: container
      });
    },

    async autoCreate() {
      // 실행중인 컨테이너가 있다면 종료
      if (this.projectInfo?.container && this.projectInfo?.container !== "" && this.projectInfo?.container !== "init") {
        this.$swal
          .fire({
            title: `실행 중인 작업이 있습니다.`,
            text: "다시 시작 하시겠습니까?",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "확인",
            cancelButtonText: "취소"
          })
          .then(async result => {
            if (result.isConfirmed) {
              await updateProjectType(this.projectInfo.id, ProjectType.AUTO);
              const res = await containerStart("bms", this.projectInfo.create_user, this.projectInfo.id);
              this.vale += res.message;
            }
          });
      } else {
        await updateProjectType(this.projectInfo.id, ProjectType.AUTO);
        const res = await containerStart("bms", this.projectInfo.create_user, this.projectInfo.id);
        this.vale += res.message;
      }

      this.SET_PROJECT({
        project_type: ProjectType.AUTO
      });

      this.$emit("start");
    },

    async menualCreate() {
      // 실행중인 컨테이너가 있다면 종료
      if (this.projectInfo?.container && this.projectInfo?.container !== "" && this.projectInfo?.container !== "init") {
        this.$swal
          .fire({
            title: `실행 중인 작업이 있습니다.`,
            text: "다시 시작 하시겠습니까?",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "확인",
            cancelButtonText: "취소"
          })
          .then(async result => {
            if (result.isConfirmed) {
              await updateProjectType(this.projectInfo.id, ProjectType.MANUAL);
            }
          });
      } else {
        await updateProjectType(this.projectInfo.id, ProjectType.MANUAL);
      }

      this.SET_PROJECT({
        project_type: ProjectType.MANUAL
      });
    },

    showContainerName(container) {
      if (container) {
        if (container.toLowerCase() === "bms") {
          return "BMS";
        } else if (container.toLowerCase() === "yoloe") {
          return "Auto NN";
        } else if (container.toLowerCase() === "codegen") {
          return "Code Gen";
        } else if (container.toLowerCase() === "imagedepoly") {
          return "Image Depoly";
        } else {
          return "";
        }
      } else {
        return "";
      }
    }
  }
};
</script>
<style lang="scss" scoped>
.end {
  background-color: #cfd2cf !important;
  color: black !important;
}

.visual {
  border-left: 3px dashed rgba(0, 0, 0, 0.12);
  border-right: 3px dashed rgba(0, 0, 0, 0.12);
  border-bottom: 3px dashed rgba(0, 0, 0, 0.12);
  z-index: 0;
}

.btn {
  z-index: 15;
}
</style>
